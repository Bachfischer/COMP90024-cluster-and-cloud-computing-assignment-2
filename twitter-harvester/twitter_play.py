import tweepy
import json
import time
from support_functions import *
from itertools import cycle


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
currentCursor=tweepy.Cursor(auths[authID].search,q=search_term,geocode=create_geocode(city_coordinates[city],"100km"))
tweets=currentCursor.items()

count=0

# print(num_of_auths)

last_tweet_id=None
while True:
	try:
		tweet=tweets.next()
		
		last_tweet_from_city[city]=tweet.id
		
		city_tweet_count[city]+=1
		
		if city_tweet_count[city]%100==0:
			print(city_tweet_count[city])

		if city_tweet_count[city]%2500==0:
			city=next(cities)
			print(city)
			if last_tweet_from_city[city]!=None:
				currentCursor=tweepy.Cursor(auths[authID].search,q=search_term,max_id=last_tweet_from_city[city]-1,geocode=create_geocode(city_coordinates[city],"100km"))
			else:
				currentCursor=tweepy.Cursor(auths[authID].search,q=search_term,geocode=create_geocode(city_coordinates[city],"100km"))
			tweets=currentCursor.items()


	except tweepy.TweepError as e:
		if e.args[0].split(" = " )[1]=="429" or e.args[0].split(" = " )[1]=="420":
			
			# print("changing Auth tokens")
			
			if int((authID)%num_of_auths)==0:
				time.sleep(60*5)
			
			authID=int((authID)%num_of_auths)+1
			
			if last_tweet_from_city[city]!=None:
				currentCursor=tweepy.Cursor(auths[authID].search,q=search_term,max_id=last_tweet_from_city[city]-1,geocode=create_geocode(city_coordinates[city],"100km"))
			else:
				currentCursor=tweepy.Cursor(auths[authID].search,q=search_term,geocode=create_geocode(city_coordinates[city],"100km"))
			tweets=currentCursor.items()
		
		if e.args[0].split(" = " )[1]=="304":
			city=next(cities)
			print(city)
			if last_tweet_from_city[city]!=None:
				currentCursor=tweepy.Cursor(auths[authID].search,q=search_term,max_id=last_tweet_from_city[city]-1,geocode=create_geocode(city_coordinates[city],"100km"))
			else:
				currentCursor=tweepy.Cursor(auths[authID].search,q=search_term,geocode=create_geocode(city_coordinates[city],"100km"))
			tweets=currentCursor.items()

	except StopIteration:
		continue

print(count)
