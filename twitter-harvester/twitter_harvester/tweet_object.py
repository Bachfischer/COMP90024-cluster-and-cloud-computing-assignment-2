import json

class Tweet_Object:
	def __init__(self,tid,city,latitude,longitude,tweet,timestamp,geo_enabled):
		self._id=tid
		self.city=city
		self.latitude=latitude
		self.longitude=longitude
		self.Flag="N"
		self.tweet=tweet
		self.timestamp=timestamp
		self.geo_enabled=geo_enabled
	
	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

