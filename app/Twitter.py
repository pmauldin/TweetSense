import tweepy

class Twitter:
	_consumer_key = 'jU99EspHuhRubNUqeQGB14wWp'
	_consumer_secret = 'cu3jZeOXzxwAzEAeOVdpzAVME9WZh3htdBjvIxn8bHD9KvfNrN'
	_access_token = '177439158-yiPRQIqAzyTu26kiY5rPPDozbbSZctd5T9Hzb3ap'
	_access_token_secret = '3ehpdolDwNj9UYCkCV2HctT9OWlYwroI17adHKHaYRN0B'

	_api = None

	def __init__(self):
		auth = tweepy.OAuthHandler(self._consumer_key, self._consumer_secret)
		auth.set_access_token(self._access_token, self._access_token_secret)

		self._api = tweepy.API(auth)

	# returns lists for words
	def getTweets(self, q, cnt=100):	
		data = self._api.search(q, count=cnt)
		result = []
		for i in data:
			tweets = []
			stringSplit = i.text.replace('\n', ' ').split(' ')
			for j in stringSplit:
				if len(j) > 1:
					if j[0] == '@':
						pass
					elif j == 'RT':
						pass
					elif j[0:4] == 'http' or j[0:4] == 'HTTP':
						pass
					else:
						tweets.append(j)
			result.append(tweets)
		return result
