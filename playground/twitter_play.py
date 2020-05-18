import tweepy
import json
import time
from support_functions import *
from itertools import cycle

def update_authid(authID,num_of_auths):
	return int((authID+1)%num_of_auths)

auths=[get_auth_object(key_list) for key_list in get_api_keys()]

num_of_auths=len(auths)

authID=0

search_term=create_search_term(get_search_terms())
# print(search_term)
city_coordinates=get_city_coordinates()

cities=list(city_coordinates.keys())

last_tweet_from_city={}
city_tweet_count={}

for city in cities:
	last_tweet_from_city[city]=None
	city_tweet_count[city]=0

cities=cycle(cities)
city=next(cities)
print(city)

# print(create_geocode(city_coordinates['melbourne'],"100km"))
currentCursor=update_cursor(auths[authID].search,search_term,create_geocode(city_coordinates[city],"100km"),last_tweet_from_city[city])
# currentCursor=tweepy.Cursor(auths[authID].search,q=search_term,geocode=create_geocode(city_coordinates[city],"100km"))
tweets=currentCursor.items()

count=0

# print(num_of_auths)
last_count=None
last_tweet_id=None
while True:
	try:
		tweet=tweets.next()
		print(tweet.created_at)
		if tweet!=None:
			count+=1
			city_tweet_count[city]+=1
		
		last_tweet_from_city[city]=tweet.id
		
		if city_tweet_count[city]%100==0:
			print(city_tweet_count[city])

		if city_tweet_count[city]%500==0:
			city=next(cities)
			print(city)
			authID=update_authid(authID,num_of_auths)
			currentCursor=update_cursor(auths[authID].search,search_term,create_geocode(city_coordinates[city],"100km"),last_tweet_from_city[city])
			tweets=currentCursor.items()
			time.sleep(2)
		elif count==last_count:
			authID=update_authid(authID,num_of_auths)
			city=next(cities)
			print(city)
			currentCursor=update_cursor(auths[authID].search,search_term,create_geocode(city_coordinates[city],"100km"),last_tweet_from_city[city])
			tweets=currentCursor.items()



	except tweepy.TweepError as e:
		print("changing Auth tokens")
		print(e)
		if authID==num_of_auths-1:
			print("sleeping")
			time.sleep(60*10)
			authID=0
		else:
			authID=update_authid(authID,num_of_auths)
		city=next(cities)
		print(city)
		currentCursor=update_cursor(auths[authID].search,search_term,create_geocode(city_coordinates[city],"100km"),last_tweet_from_city[city])
		tweets=currentCursor.items()
	except StopIteration:
		continue