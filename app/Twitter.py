#coding: utf8

import tweepy
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

	def getEachTweet(self):
		return self.tweets

	def getTweets(self, q, cnt=1):
		if self.dateFrom == '' or self.dateTo == '':
			return ''

		user_last_id = 0
		data = self._twitter_api.search(q, count=cnt, until='2015-01-12', result_type='popular', lang='en')
		tweets = ""
		j = 0
		for i in data:
			print i.created_at
			j += 1
			tweets += i.text
			self.tweets.append(i.text)
			if j == len(data):
				user_last_id = i.id

		# print tweets
		return tweets, user_last_id

	def getScore(self, chars):
		response = self._alchemy_api.sentiment('text', chars)
		return response['docSentiment']['score']

	def setDate(self, _from, _to):
		self.dateFrom = _from
		self.dateTo = _to





t = Twitter()
t.setDate('d','e')
a, b = t.getTweets('google', 100)
print len(t.getEachTweet())
print a.encode('utf-8')
print b
print t.getScore(a)
