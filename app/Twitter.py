#coding: utf8

import tweepy
import time, datetime
import calendar
import six
# from alchemyapi import AlchemyAPI

class Twitter:
	_consumer_key = 'jU99EspHuhRubNUqeQGB14wWp'
	_consumer_secret = 'cu3jZeOXzxwAzEAeOVdpzAVME9WZh3htdBjvIxn8bHD9KvfNrN'
	_access_token = '177439158-yiPRQIqAzyTu26kiY5rPPDozbbSZctd5T9Hzb3ap'
	_access_token_secret = '3ehpdolDwNj9UYCkCV2HctT9OWlYwroI17adHKHaYRN0B'

	_twitter_api = None
	# _alchemy_api = None

	dateFrom = ''
	dateTo = ''
	tweets = []

	def __init__(self):
		auth = tweepy.OAuthHandler(self._consumer_key, self._consumer_secret)
		auth.set_access_token(self._access_token, self._access_token_secret)

		self._twitter_api = tweepy.API(auth)
		# self._alchemy_api = AlchemyAPI()

	def getTweets(self, q, cnt):
		now = datetime.datetime.now()
		tweets = []
		epochToNow = int(time.time())
		for days in range(0,7):
			# Will break on days < the 7th
			start_date = str(now.year) + '-' + str(now.month) + '-' + str(now.day - (days + 1))
			end_date = str(now.year) + '-' + str(now.month) + '-' + str(now.day - days)
			data = self._twitter_api.search(q, count=cnt, since=start_date, until=end_date)
			
			for i in data:
				t = time.strptime(str(i.created_at), "%Y-%m-%d %H:%M:%S")
				epochToTweet = calendar.timegm(t)
				text = i.text
				daysPast = float(epochToTweet - epochToNow) / 86400
				if text[:2] == 'u\'':
					text = i.text.encode('utf-8')
				tweets.append((daysPast, text))
		return tweets

	def checkTerm(self, q):
		try:
			return len(self._twitter_api.search(q, count=6)) >= 6
		except (e):
			print False	

# t = Twitter()

# print t.getTweets('apple', 25)
