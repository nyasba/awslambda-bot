# -*- coding: utf-8 -*-

import requests
import logging
import json
import urllib

api_token = '<api token>'

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def post_message(room_id, message):
	url = 'https://api.chatwork.com/v1/rooms/{0}/messages'.format(room_id)
	headers = { 'X-ChatWorkToken' : api_token }
	payload = { 'body' : message }
	
	
	r = requests.post(url, headers=headers, data=payload )
	logger.info(r.text)

def lambda_handler(event, context):
	
	#bucket = event['Records'][0]['s3']['bucket']['name']

	#日本語を含むファイル名だと文字化けしてしまいます
	key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key']).decode('utf8')

	logger.info('[key1]' + event['Records'][0]['s3']['object']['key'])
	logger.info('[key2]' + urllib.unquote_plus(event['Records'][0]['s3']['object']['key']))
	logger.info('[key3]' + key)
	logger.info('[key3]' + key.encode('utf8'))
	
	post_message('<room id>', u'S3に{0}がアップされました'.format(key))
		