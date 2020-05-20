import tweepy
from db_constants import *
from support_functions import *

class TwitterStreamListener(tweepy.StreamListener):

	def __init__(self):
		self.count=0
		super(TwitterStreamListener, self).__init__()
	
	# def on_status(self, status):
	# 	print(status.user)
	# 	self.count+=1

	def on_error(self, status_code):
		if status_code == 420 or status_code==429:
			self.database_client.close_connection()
			return False

	def on_data(self,data):
		if self.count==10:
			return False
		else:
			print(data)
			self.count+=1
			return True

