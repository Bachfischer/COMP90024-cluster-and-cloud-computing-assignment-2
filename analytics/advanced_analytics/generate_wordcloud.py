#
# Part of Assignment 2 - COMP90024 course at The University of Melbourne 
#
# Cluster and Cloud Computing - Team 24 
# 
# Authors: 
#
#  * Liam Simon (Student ID: 1128453)
#  * Rejoy Benjamin (Student ID: 1110935)
#  * Parikshit Diwan (Student ID: 1110497)
#  * Colin McLean (Student ID: 1139518)
#  * Matthias Bachfischer (Student ID: 1133751)
#
# Location: Melbourne
#
from twitter-harvester.twitter_harvester.db_client import DBClient
from twitter-harvester.twitter_harvester.db_constants import *
import json
from wordcloud import WordCloud, STOPWORDS
import re
import matplotlib.pyplot as plt
import preprocessor as p

def generate_wordcloud(list_of_texts):
	p.set_options(p.OPT.URL, p.OPT.EMOJI)
	for i in range(len(list_of_texts)):
		list_of_texts[i]=p.clean(list_of_texts[i])
	raw_string = ''.join(list_of_texts)
	raw_string=remove_hash_rate(raw_string)
	no_links = re.sub(r'http\S+', '', raw_string)
	no_unicode = re.sub(r"\\[a-z][a-z]?[0-9]+", '', no_links)
	no_special_characters = re.sub('[^A-Za-z ]+', '', no_unicode)
	words = no_special_characters.split(" ")
	words = [w for w in words if len(w) > 2]
	words = [word for word in words if not word in STOPWORDS]
	wc = WordCloud(background_color="white", max_words=100)
	clean_string = ','.join(words)
	plt.imshow(wc.generate(clean_string), interpolation='bilinear')
	plt.axis("off")
	plt.show()

def remove_hash_rate(text):
	return text.replace('@',' ').replace('#',' ')


cities=["melbourne","sydney","perth","canberra","adelaide","brisbane"]

db_client= DBClient(DATABASE_USERNAME, DATABASE_PASSWORD, url=DATABASE_URL)

dataset={}


# for city in cities:
# 	dataset[city]=[]

fp=open('raw_data.json','r')
for line in fp:
	dataset=line
dataset=json.loads(dataset)

# for city in cities: 
# 	database_result=db_client.get_database(REPOSITORY_DATABASE).get_query_result({'city': {'$eq': city }})
# 	for doc in database_result:
# 		text=json.loads(doc['tweet'])['text'].lower()
# 		dataset[city].append(text)
# 	print(city+" "+str(len(dataset[city])))

# with open('raw_data.json', 'w') as fp:
# 	json.dump(dataset, fp)

# dataset=None
# fp=open('raw_data.json','r')
# for line in fp:
# 	dataset=line
# dataset=json.loads(dataset)
for city in cities:
	generate_wordcloud(dataset[city])
	
