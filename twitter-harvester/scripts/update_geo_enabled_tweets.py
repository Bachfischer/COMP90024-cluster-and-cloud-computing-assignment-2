from DBClient import DBClient
from db_constants import *
import json

database_client= DBClient(DATABASE_USERNAME, DATABASE_PASSWORD, url=DATABASE_URL)
twitter_database=database_client.get_database(REPOSITORY_DATABASE)

for doc in twitter_database:
	tweet=json.loads(doc['tweet'])
	if tweet['coordinates']!=None:
		coordinates=tweet['coordinates']['coordinates']
		doc['latitude']=str(coordinates[1])
		doc['longitude']=str(coordinates[0])
		doc['geo_enabled']=True
	else:
		doc['geo_enabled']=False
	doc.save()
database_client.close_connection()
