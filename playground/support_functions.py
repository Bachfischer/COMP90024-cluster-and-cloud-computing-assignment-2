import tweepy

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
		city_coordinate_dict[data[0]]=data[1:3]
	return city_coordinate_dict

def get_search_terms():
	f=open('search_phrases.txt','r')
	search_phrases=[]
	for line in f:
		search_phrases.append(line)
	return search_phrases

def create_search_term(searh_terms):
	search_term=None
	for term in search_terms:
		if search_term==None:
			search_term=term
		else:
			search_term=search_term or term

def create_geocode(coordinates,distance):
	return coordinates[0]+","+coordinates[1]+","+distance