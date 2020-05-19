import tweepy
import datetime


#generate auth objects
def get_auth_object(keys):
	auth=tweepy.OAuthHandler(keys[0],keys[1])
	auth.set_access_token(keys[2],keys[3])
	return tweepy.API(auth)


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
