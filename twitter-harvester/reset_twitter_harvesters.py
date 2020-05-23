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

from twitter_harvester.db_client import DBClient
from twitter_harvester.db_constants import *

database_client= DBClient(DATABASE_USERNAME, DATABASE_PASSWORD, url=DATABASE_URL)
twitter_database=database_client.get_database('twitter_credentials')
for doc in twitter_database:
	doc['in_use']=False
	doc.save()
cities_database=database_client.get_database('cities')
for doc in cities_database:
	doc['in_use']=False
	doc.save()
database_client.close_connection()
