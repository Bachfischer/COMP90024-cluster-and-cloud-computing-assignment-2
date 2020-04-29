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

authID=0

search_term="climatechange" or "globalwarming"
currentCursor=tweepy.Cursor(auths[authID].search,q=search_term,lang="en")
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
			if authID>0 and int((authID)%num_of_auths)==0:
				time.sleep(300)
			authID=int((authID+1)%num_of_auths)
			print(authID)
			print(last_tweet_id)
			currentCursor=tweepy.Cursor(auths[authID].search,q=search_term,lang="en",max_id=last_tweet_id-1)
			tweets=currentCursor.items()
	except StopIteration:
		continue

print(count)
