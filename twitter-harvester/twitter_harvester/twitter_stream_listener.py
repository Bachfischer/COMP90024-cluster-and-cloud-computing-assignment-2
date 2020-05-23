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

import tweepy
from db_constants import *
from support_functions import *

class TwitterStreamListener(tweepy.StreamListener):

	def __init__(self):
		self.count=0
		super(TwitterStreamListener, self).__init__()
	
	def on_status(self, status):
        db_client = DBClient('admin', 'data-miner!', url='http://172.26.133.36:5984/')

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

