#coding: utf8

import tweepy
import time, datetime
import calendar
import six
from alchemyapi import AlchemyAPI

class Twitter:
	_consumer_key = 'jU99EspHuhRubNUqeQGB14wWp'
	_consumer_secret = 'cu3jZeOXzxwAzEAeOVdpzAVME9WZh3htdBjvIxn8bHD9KvfNrN'
	_access_token = '177439158-yiPRQIqAzyTu26kiY5rPPDozbbSZctd5T9Hzb3ap'
	_access_token_secret = '3ehpdolDwNj9UYCkCV2HctT9OWlYwroI17adHKHaYRN0B'

	_twitter_api = None
	_alchemy_api = None

	dateFrom = ''
	dateTo = ''
	tweets = []

	def __init__(self):
		auth = tweepy.OAuthHandler(self._consumer_key, self._consumer_secret)
		auth.set_access_token(self._access_token, self._access_token_secret)

		self._twitter_api = tweepy.API(auth)
		self._alchemy_api = AlchemyAPI()

	def getTweets(self, q):
		now = datetime.datetime.now()
		data_list = []
		for days in range(0,7):
			formatted_now = str(now.year) + '-' + str(now.month) + '-' + str(now.day - days + 1)
			data = self._twitter_api.search(q, count=30, result_type='popular', until=formatted_now)
			tweets = ''
			for i in data:
				tweets += i.text + ' '
			res = self._alchemy_api.sentiment("text", tweets)
			data_list.append((-days, float(res['docSentiment']['score'])))
		return data_list

