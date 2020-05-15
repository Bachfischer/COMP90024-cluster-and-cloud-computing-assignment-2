from DBClient import DBClient
from Tweet_Object import Tweet_Object
from support_functions import *
import datetime
import time
import json
import jsons

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

def get_twitter_auth_client(database_client):
	while True:
		twitter_credentials=database_client.get_query_result('twitter_credentials',{'in_use': {'$eq': False }})
		if len(twitter_credentials)>0:
			valid_credentials,min_diff=get_valid_credentials(twitter_credentials)
			if valid_credentials!=None:
				database_client.modify_record('twitter_credentials',valid_credentials['_id'],['in_use'],[True])
				auth=get_auth_object([valid_credentials[key] for key in ['consumer_key','consumer_secret','access_token_key','access_token_secret']])
				return auth,valid_credentials['_id']
			else:
				time.sleep(int(15-min_diff)*60)
		else:
			time.sleep(180)



def get_city_to_search(database_client):
	cities=database_client.get_query_result('cities',{'in_use': {'$eq': False }})
	if len(cities)>0:
		cities=sorted(cities,key=lambda i:get_time_diff(datetime.datetime.strptime(i['last_use'], datetimeFormat),datetime.datetime.now()),reverse=True)
		database_client.modify_record('cities',cities[0]['_id'],['in_use'],[True])
		return cities[0]

def get_last_tweet_id(database_client,city):
	result=database_client.get_database('twitter_example').get_query_result({'city': {'$eq': city }})
	# result=database_client.get_query_result('twitter_example',,)
	if len(list(result))>0:
		return list(result)[0]['_id']
	return None




db_client = DBClient('admin', 'data-miner!', url='http://172.26.132.56:5984/')

search_term="climatechange" or "globalwarming"

auth,credential_id=get_twitter_auth_client(db_client)
print("got auth")
city=get_city_to_search(db_client)
print(city['_id'])
currentCursor=update_cursor(auth.search,search_term,create_geocode([city['lat'],city['long']],"100km"),get_last_tweet_id(db_client,city['_id']))
tweets=currentCursor.items()
print("got cursor")

while True:
	try:
		tweet=tweets.next()
		myObject=Tweet_Object(str(tweet.id),city['_id'],city['lat'],city['long'],json.dumps(tweet._json),tweet.created_at)
		db_client.add_record('twitter_example',jsons.dump(myObject))
		print("record_added")
	except tweepy.TweepError as e:
		db_client.modify_record('twitter_credentials',credential_id,['in_use','last_used'],[False,datetime.datetime.now()])
		db_client.modify_record('cities',city['_id'],['in_use','last_used'],[False,datetime.datetime.now()])
			
		auth,credential_id=get_twitter_auth_client(db_client)
		city=get_city_to_search(db_client)
			
		currentCursor=update_cursor(auth.search,search_term,create_geocode([city['lat'],city['long']],"100km"),get_last_tweet_id(city['_id']))
		tweets=currentCursor.items()
	except StopIteration:
		continue


