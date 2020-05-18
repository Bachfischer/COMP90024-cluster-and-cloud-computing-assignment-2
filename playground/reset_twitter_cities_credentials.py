from DBClient import DBClient
from db_constants import *

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
