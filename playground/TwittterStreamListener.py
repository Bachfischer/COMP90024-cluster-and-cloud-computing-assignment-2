import tweepy
import json

class TwitterStreamListener(tweepy.StreamListener):

	def on_status(self, status):
		print(json.dumps(status._json))

	def on_error(self, status_code):
		if status_code == 420:
			return False

