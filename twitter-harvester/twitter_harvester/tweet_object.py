#!/usr/bin/env python
#
# Part of Assignment 2 - COMP90024 course at The University of Melbourne 
#
# Cluster and Cloud Computing - Team 24 
# 
# Authors: 
#
#  * Liam Simon (Student ID: 1128453)
#  * Rejoy Benjamin (Student ID: 1110935)
#  * Parikshit Diwan (Student ID: 1110497)
#  * Colin McLean (Student ID: 1139518)
#  * Matthias Bachfischer (Student ID: 1133751)
#
# Location: Melbourne
#

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

