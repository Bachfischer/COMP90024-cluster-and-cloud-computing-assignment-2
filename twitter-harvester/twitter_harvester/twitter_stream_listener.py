import tweepy
from db_constants import *
from support_functions import *

class TwitterStreamListener(tweepy.StreamListener):

	def __init__(self):
		self.count=0
		super(TwitterStreamListener, self).__init__()
	
<<<<<<< HEAD
	# def on_status(self, status):
	# 	print(status.user)
	# 	self.count+=1
=======
	def on_status(self, status):
        db_client = DBClient('admin', 'data-miner!', url='http://172.26.133.36:5984/')
>>>>>>> 987a0a8b60d0f9b88e8936f52a13b9d51387ae88

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

