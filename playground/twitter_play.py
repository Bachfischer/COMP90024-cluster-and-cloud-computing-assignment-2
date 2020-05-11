import tweepy
import json
import time

#get api keys stored in api_keys.txt
def get_api_keys():
	f=open('api_keys.txt','r')
	apis=[]
	line_count=0
	for line in f:
		if line_count==0:
			line_count+=1
		else:
			keys=line.split(',')
			keys=[key.strip() for key in keys]
			apis.append(keys)
	return apis


#generate auth objects
def get_auth_object(keys):
	auth=tweepy.OAuthHandler(keys[0],keys[1])
	auth.set_access_token(keys[2],keys[3])
	return tweepy.API(auth)


auths=[get_auth_object(key_list) for key_list in get_api_keys()]

num_of_auths=len(auths)

authID=1

search_term="climate change"
currentCursor=tweepy.Cursor(auths[authID].search,q=search_term,geocode="-37.817403,144.956776,100km")
tweets=currentCursor.items()
count=0

print(num_of_auths)

last_tweet_id=None
while True:
	try:
		tweet=tweets.next()
		last_tweet_id=tweet.id
		count+=1
		if count%100==0:
			print(count)

	except tweepy.TweepError as e:
		if e.args[0].split(" = " )[1]=="429" :
			print("changing Auth tokens")
			if int((authID)%num_of_auths)==0:
				#print("sleeping")
				time.sleep(60*5)
			authID=int((authID)%num_of_auths)+1
			print(authID)
			if last_tweet_id!=None:
				currentCursor=tweepy.Cursor(auths[authID].search,q=search_term,max_id=last_tweet_id-1,geocode="-37.817403,144.956776,50km")
			else:
				currentCursor=tweepy.Cursor(auths[authID].search,q=search_term,geocode="-37.817403,144.956776,50km")
			tweets=currentCursor.items()
	except StopIteration:
		continue

print(count)
