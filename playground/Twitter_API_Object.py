import tweepy

class Twitter_API_Object:
	def __init__(self,consumer_key,consumer_secret,access_token_key,access_token_secret):
		self.consumer_key=consumer_key
		self.consumer_secret=consumer_secret,
		self.access_token_key=access_token_key
		self.access_token_secret=access_token_secret
		self.auth=self.create_auth()

	def create_auth(self):
		auth=tweepy.OAuthHandler(self.consumer_key,self.consumer_secret)
		auth.set_access_token(self.access_token_key,self.access_token_secret)
		return tweepy.API(auth)