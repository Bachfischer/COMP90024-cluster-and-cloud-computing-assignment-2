import tweepy
import datetime
import string

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

def get_city_coordinates():
	f=open('cities.txt','r')
	city_coordinate_dict={}
	for line in f:
		data=line.split(',')
		data=[term.strip() for term in data]
		city_coordinate_dict[data[0]]=data[1:3]
	return city_coordinate_dict

def get_search_terms():
	f=open('search_phrases.txt','r')
	search_phrases=[]
	for line in f:
		search_phrases.append(line.strip())
	return search_phrases

def create_search_term(search_terms):
	search_term=None
	for term in search_terms:
		if search_term==None:
			search_term=term
		else:
			search_term=search_term+" OR "+term
	return search_term

def create_geocode(coordinates,distance):
	return coordinates[0]+","+coordinates[1]+","+distance

def update_cursor(auth_object,search_term,geocode,last_tweet_id,max_tweet_id):
	if last_tweet_id!=None:
		currentCursor=tweepy.Cursor(auth_object,q=search_term,max_id=last_tweet_id-1,geocode=geocode)
	elif max_tweet_id!=None:
		currentCursor=tweepy.Cursor(auth_object,q=search_term,since_id=max_tweet_id+1,geocode=geocode)
	else:
		currentCursor=tweepy.Cursor(auth_object,q=search_term,geocode=geocode)
	return currentCursor

def decide_whether_text_match(text,search_terms):
	for term in search_terms:
		if term in ''.join(e for e in text.lower() if e.isalnum()):
			return True
	return False

