#textblob is a awesome python library for processing textual data
#It is useful to do natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis etc

import csv
import os
from os import listdir
from os.path import isfile,join

no_of_reviews = 0
review_json = dict()
column = []


amazon_reviews_file =  open(r'C:\Users\iimra\Documents\NLTK\Helpful_All_review_details (1).csv','rb')
for row in amazon_reviews_file:
	no_of_reviews += 1
	print(row)
	review_json['reviewerID'] = row[9]
	review_json['asin']=row[1]
	review_json['helpful']=row[5]
	review_json['reviewText']=row[8]
	review_json['overallRating']=row[6]
	
	
print(no_of_reviews)
print(review_json)
