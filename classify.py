import nltk

import random #to shuffle up dataset

from nltk.corpus import movie_reviews

#print(movie_reviews)
#documents = []

#for category in movie_reviews.categories():
	# for fileid in movie_reviews.fileids(category):
		# documents.append[list(movie_reviews.words(fileid)),category)]
		
		
documents = [(list(movie_reviews.words(fileid)),category)
			for category in movie_reviews.categories()
			for fileid in movie_reviews.fileids(category)]
			
			
random.shuffle(documents)

#print(documents)

all_words = []
for w in movie_reviews.words():
	all_words.append(w.lower())

	
all_words = nltk.FreqDist(all_words)

print(all_words.most_common(15))

print(all_words["stupid"])