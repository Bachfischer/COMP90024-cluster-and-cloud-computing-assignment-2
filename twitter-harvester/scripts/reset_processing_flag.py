from twitter_harvester.db_client import DBClient
from twitter_harvester.db_constants import *
import json

database_client= DBClient(DATABASE_USERNAME, DATABASE_PASSWORD, url=DATABASE_URL)
twitter_database=database_client.get_database(REPOSITORY_DATABASE)


for doc in twitter_database:
	print("Processing document: " +  doc['_id'])
	doc['Flag']="N"
	doc.save()
database_client.close_connection()
