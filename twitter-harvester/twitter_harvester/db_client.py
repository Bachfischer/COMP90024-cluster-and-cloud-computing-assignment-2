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

from cloudant.client import CouchDB

class DBClient:
	def __init__(self,username,password,url):
		self.client= CouchDB(username,password, url=url, connect=True)

	def get_session(self):
		return self.client.session()

	def get_database(self,database_name):
		return self.client[database_name]

	def get_client(self):
		return self.client

	def get_query_result(self,database_name,selector,sort=None):
		if sort==None:
			return list(self.get_database(database_name).get_query_result(selector))
		return list(self.get_database(database_name).get_query_result(selector,sort=sort))

	def modify_record(self,database_name,record_id,column_names,new_column_values):
		record=self.get_database(database_name)[record_id]
		for i in range(len(column_names)):
			record[column_names[i]]=new_column_values[i]
		record.save()

	def close_connection(self):
		self.client.disconnect()


	def add_record(self,database_name,record):
		if record['_id'] not in self.get_database(database_name):
			doc=self.get_database(database_name).create_document(record)
			return True
		return False