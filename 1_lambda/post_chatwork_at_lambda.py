# -*- coding: utf-8 -*-

import requests
import logging

api_token = '{your api token}'

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def post_message(room_id, message):
	url = 'https://api.chatwork.com/v1/rooms/{0}/messages'.format(room_id)
	headers = { 'X-ChatWorkToken' : api_token }
	payload = { 'body' : message }
	
	
	r = requests.post(url, headers=headers, data=payload )
	logger.info(r.text)

def lambda_handler(event, context):
	post_message('{room_id}', 'Lambdaからも成功！ ﾔﾀ──v(-∀-)v──★')