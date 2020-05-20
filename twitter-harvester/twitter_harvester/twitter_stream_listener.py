import tweepy

class TwitterStreamListener(tweepy.StreamListener):

	def __init__(self,database_client,city):
		self.database_client=database_client
		self.city=city
	
	def on_status(self, status):
        db_client = DBClient('admin', 'data-miner!', url='http://172.26.133.36:5984/')

    def on_error(self, status_code):
        if status_code == 420:
        	self.database_client.close_connection()
            return False

