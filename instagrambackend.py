#import requests
#r = requests.get("https://instagram.com/alexlim")
#print r.text

a = {
	'hello':'world',
	'halp': 3,
	'hi': True,
	'we': [],
	'blah': ["one", "two", "three"],
	'dicts': {},
	'dicts2': {
		'stuff': 'cool'
	}
}
print a.get('dicts2').get('stuff')
print a['dicts2']['stuff']
#print a['hh']

import json
b = """{\"hello\":\"world\"}"""
c = json.loads(b)
print b

print c.get("hello")

d = json.dumps(c)
print d