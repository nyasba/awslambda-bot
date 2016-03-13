# -*- coding: utf-8 -*-

import doctest
import requests

api_token = '{your api token}'

# コマンドで実行する場合はこれ
# curl --insecure -X POST -H "X-ChatWorkToken: {your api token}" -d "body=Test" "https://api.chatwork.com/v1/rooms/{room_id}/messages"

def post_message(room_id, message):
	'''
	chatworkへメッセージを投稿する
	
	>>> post_message('{room id}', '☆-ヽ(*´∀｀)八(´∀｀*)ノｲｴｰｲ')
	
	'''
	
	url = 'https://api.chatwork.com/v1/rooms/{0}/messages'.format(room_id)
	headers = { 'X-ChatWorkToken' : api_token }
	payload = { 'body' : message }
	
	r = requests.post(url, headers=headers, data=payload )

if __name__ == "__main__":
	doctest.testmod()
	