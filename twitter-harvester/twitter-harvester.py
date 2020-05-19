from db_client import DBClient
from tweet_object import Tweet_Object
from support_functions import *
from db_constants import *
import datetime
import time
import json
import jsons
import random

datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'

def get_time_diff(date_time_1,date_time_2):
	difference_in_seconds = abs(time.mktime(date_time_1.timetuple()) - time.mktime(date_time_2.timetuple()))
	difference_in_minutes = difference_in_seconds / 60
	return difference_in_minutes

def get_valid_credentials(list_of_credentials):
	min_diff=0
	for cred in list_of_credentials:
		time_diff=get_time_diff(datetime.datetime.strptime(cred['last_used'], datetimeFormat),datetime.datetime.now())
		if time_diff>=15:
			return cred,time_diff
		else:
			min_diff=max(min_diff,time_diff)
	return None, min_diff

def get_twitter_auth_client():
	database_client= DBClient(DATABASE_USERNAME, DATABASE_PASSWORD, url=DATABASE_URL)
	while True:
		twitter_credentials=database_client.get_query_result(CREDENTIALS_DATABASE,{'in_use': {'$eq': False }})
		if len(twitter_credentials)>0:
			valid_credentials,min_diff=get_valid_credentials(twitter_credentials)
			if valid_credentials!=None:
				database_client.modify_record(CREDENTIALS_DATABASE,valid_credentials['_id'],['in_use'],[True])
				auth=get_auth_object([valid_credentials[key] for key in ['consumer_key','consumer_secret','access_token_key','access_token_secret']])
				database_client.close_connection()
				return auth,valid_credentials['_id']
			else:
				print("sleeping "+str(int(15-min_diff)*60) )
				time.sleep(int(15-min_diff)*60+60)
		else:
			print("sleeping 180")
			time.sleep(180)
			



def get_city_to_search():
	database_client= DBClient(DATABASE_USERNAME, DATABASE_PASSWORD, url=DATABASE_URL)
	cities=database_client.get_query_result(CITIES_DATABASE,{'in_use': {'$eq': False }})
	if len(cities)>0:
		cities=sorted(cities,key=lambda i:get_time_diff(datetime.datetime.strptime(i['last_used'], datetimeFormat),datetime.datetime.now()),reverse=True)
		database_client.modify_record(CITIES_DATABASE,cities[0]['_id'],['in_use'],[True])
		database_client.close_connection()
		return cities[0]

def get_last_tweet_id(database_client,city):
	# database_client= DBClient('admin', 'data-miner!', url='http://172.26.132.56:5984/')
	result=database_client.get_database(REPOSITORY_DATABASE).get_query_result({'city': {'$eq': city }})
	# result=database_client.get_query_result('twitter_example',,)
	# database_client.close_connection()
	if len(list(result))>0:

		return int(list(result)[0]['_id'])
	return None


def get_search_term():
	database_client= DBClient(DATABASE_USERNAME, DATABASE_PASSWORD, url=DATABASE_URL)
	result=database_client.get_database(SEARCH_TERM_DATABASE)[SEARCH_TERM]
	
	phrase=create_search_term(result['phrases'])
	database_client.close_connection()
	return phrase

def choose_cursor(database_client,auth,city,search_term):
	if "back" in city["available_options"]:
		return update_cursor(auth.search,search_term,create_geocode([city['lat'],city['long']],"100km"),get_last_tweet_id(db_client,city['_id']),None)
	else:
		i=random.randint(0,1)
		#print(i)
		if city["available_options"][i]=='forward':
			return update_cursor(auth.search,search_term,create_geocode([city['lat'],city['long']],"100km"),None,int(city["max_id"]))
		else:
			return update_cursor(auth.search,search_term,create_geocode([city['lat'],city['long']],"100km"),None,None)


# db_client = DBClient('admin', 'data-miner!', url='http://172.26.132.56:5984/')
search_term=get_search_term()
# search_term="climatechange" or "globalwarming" or "climateaction" or "climatejustice"

auth,credential_id=get_twitter_auth_client()
print("got auth")
city=get_city_to_search()
print("got city")
print(city["_id"])
db_client= DBClient(DATABASE_USERNAME, DATABASE_PASSWORD, url=DATABASE_URL)
currentCursor=choose_cursor(db_client,auth,city,search_term)
min_id=get_last_tweet_id(db_client,city['_id'])
db_client.close_connection()
tweets=currentCursor.items()

while True:
	try:
		print("here to add")
		for tweet in tweets:
			t=json.loads(json.dumps(tweet._json))
			myObject=None
			if t['coordinates']!=None:
				myObject=Tweet_Object(str(tweet.id),city['_id'],str(t['coordinates']['coordinates'][1]),str(t['coordinates']['coordinates'][0]),json.dumps(tweet._json),tweet.created_at,True)
			else:
				myObject=Tweet_Object(str(tweet.id),city['_id'],city['lat'],city['long'],json.dumps(tweet._json),tweet.created_at,False)
			db_client= DBClient(DATABASE_USERNAME, DATABASE_PASSWORD, url=DATABASE_URL)
			if db_client.add_record(REPOSITORY_DATABASE,jsons.dump(myObject)):
				print("tweet added")
				if int(city['max_id'])<tweet.id:
					city['max_id']=str(tweet.id)
			db_client.close_connection()
		time.sleep(random.randint(0,4))
		db_client= DBClient(DATABASE_USERNAME, DATABASE_PASSWORD, url=DATABASE_URL)
		
		if min_id==get_last_tweet_id(db_client,city['_id']) and len(city['available_options'])==3:
			city['available_options'].remove('back')

		db_client.modify_record(CITIES_DATABASE,city['_id'],['in_use','last_used','max_id','available_options'],[False,datetime.datetime.now().strftime(datetimeFormat),city['max_id'],city['available_options']])
		db_client.close_connection()
		city=get_city_to_search()
		print("got city")
		print(city["_id"])
		search_term=get_search_term()
		db_client= DBClient(DATABASE_USERNAME, DATABASE_PASSWORD, url=DATABASE_URL)
		currentCursor=choose_cursor(db_client,auth,city,search_term)
		min_id=get_last_tweet_id(db_client,city['_id'])
		db_client.close_connection()
		tweets=currentCursor.items()
			
	except tweepy.TweepError as e:
		print(e)
		time.sleep(random.randint(0,4))
		db_client= DBClient(DATABASE_USERNAME, DATABASE_PASSWORD, url=DATABASE_URL)
		if min_id==get_last_tweet_id(db_client,city['_id']) and len(city['available_options'])==3:
			city['available_options'].remove('back')
		db_client.modify_record(CREDENTIALS_DATABASE,credential_id,['in_use','last_used'],[False,datetime.datetime.now().strftime(datetimeFormat)])
		db_client.modify_record(CITIES_DATABASE,city['_id'],['in_use','last_used','max_id','available_options'],[False,datetime.datetime.now().strftime(datetimeFormat),city['max_id'],city['available_options']])
		db_client.close_connection()
		auth,credential_id=get_twitter_auth_client()
		print("got auth")
		city=get_city_to_search()
		print("got city")
		print(city["_id"])
		
		db_client= DBClient(DATABASE_USERNAME, DATABASE_PASSWORD, url=DATABASE_URL)
		currentCursor=choose_cursor(db_client,auth,city,search_term)
		min_id=get_last_tweet_id(db_client,city['_id'])
		db_client.close_connection()
		tweets=currentCursor.items(100)
	except StopIteration:
		continue


