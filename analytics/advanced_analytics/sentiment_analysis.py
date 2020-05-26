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

from textblob import TextBlob
import json
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


cities=["melbourne","sydney","perth","canberra","adelaide"]

fp=open('raw_data.json','r')

for line in fp:
	dataset=line
dataset=json.loads(dataset)

polarity_score={}
subjectivity_score={}

for city in cities:
	polarity_score[city]=[]
	subjectivity_score[city]=[]

for city in cities:
	for text in dataset[city]:
		testimonial=TextBlob(text)
		polarity_score[city].append(testimonial.sentiment.polarity)
		subjectivity_score[city].append(testimonial.sentiment.subjectivity)
	print(city)
	print(sum(polarity_score[city])/len(dataset[city]))
	print(sum(subjectivity_score[city])/len(dataset[city]))
	sns.distplot(np.array(polarity_score[city]),hist=False)
	plt.title("Polarization metric for "+city)
	plt.xlabel("Score")
	plt.ylabel("Frequency")
	plt.show()
	sns.distplot(np.array(subjectivity_score[city]),hist=False)
	plt.title("Subjectivity metric for "+city)
	plt.xlabel("Score")
	plt.ylabel("Frequency")
	plt.show()
