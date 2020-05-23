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