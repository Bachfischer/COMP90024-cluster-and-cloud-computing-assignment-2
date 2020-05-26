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
