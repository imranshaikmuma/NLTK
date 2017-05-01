import nltk
import csv

review_file = open(r"amazon product.xlsx",'rb')
product_reviews= csv.reader(review_file)
reviews = []
for each in product_reviews:
	reviews.append(each)
	
print(reviews)
	