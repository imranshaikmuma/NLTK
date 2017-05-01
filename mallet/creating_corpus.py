import csv
import os
from os import listdir
from os.path import isfile,join


number_of_reviews_total =0
category = []


with open(os.path.join('data','Helpful_Verified_review_details.csv')) as inputfile:
	reviews = csv.reader(inputfile)
	next(reviews)
	for row	 in reviews:
		
		category.append(row[0])
		
		inputpath = os.path.join('data','amazon_reviews')
		
		filenames = [f for f in listdir(inputpath) if isfile(join(inputpath,f))]
		
		review_files = len(filenames)
		
		review_files +=1
		
		
		#textfile = row[0]+'_'+str(review_files)+'.txt'
		textfile = str(review_files)+'.txt'
		print(os.path.join('data','amazon_reviews',textfile))
		
		with open(os.path.join('data','amazon_reviews',textfile),'w') as file:
			file.write(row[6])
			
		number_of_reviews_total +=1
		
print(number_of_reviews_total)
			
		
		
		

		
			
	
		
