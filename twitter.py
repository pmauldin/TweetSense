import tweepy
import re

consumer_key = 'jU99EspHuhRubNUqeQGB14wWp'
consumer_secret = 'cu3jZeOXzxwAzEAeOVdpzAVME9WZh3htdBjvIxn8bHD9KvfNrN'

access_token = '177439158-yiPRQIqAzyTu26kiY5rPPDozbbSZctd5T9Hzb3ap'
access_token_secret = '3ehpdolDwNj9UYCkCV2HctT9OWlYwroI17adHKHaYRN0B'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

result = api.search('bus', count=100)

for i in result:
	print i.text.encode('utf-8')