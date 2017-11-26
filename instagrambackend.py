#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import requests
import re
import json

#http://jsonviewer.stack.hu/
r = requests.get("https://instagram.com/alexlim")
html_page = r.text

result = re.search('window._sharedData = (.*);</script>', html_page)


insta_json = json.loads(result.group(1))

insta_user  = insta_json['entry_data']['ProfilePage'][0]['user']

api_results = {
	'biography': insta_user['biography'],
	'external_url':insta_user['external_url'],
	'followed_by':insta_user['followed_by']['count'],
	'follows':insta_user['follows']['count'],
	'full_name':insta_user['full_name'],
	'id':insta_user['id'],
	'profile_pic':insta_user['profile_pic_url'],
	'username':insta_user['username']
}
print api_results