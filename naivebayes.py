import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from collections import defaultdict
import numpy as np

split = 0.8

def word_feats(words):
	feats = defaultdict(lambda: False)
	for word in words:
		feats[word] = True
	return feats

posids = movie_reviews.fileids('pos')
negids = movie_reviews.fileids('neg')

print('posids',posids)
print('negids',negids)
posfeats = [(word_feats(movie_reviews.words(fileids=[f])),'pos')
			for f in posids]
negfeats = [(word_feats(movie_reviews.words(fileids=[f])),'neg')
			for f in negids]
			
print('posfeats',posfeats[1:10])

cutoff = int(len(posfeats)*split)

print('cutoff',cutoff)

trainfeats = negfeats[:cutoff]+posfeats[:cutoff]
testfeats= negfeats[cutoff:]+posfeats[cutoff:]

print('Train on %d instances\nTest on %d instances'%(len(trainfeats),len(testfeats)))

classifier = NaiveBayesClassifier.train(trainfeats)

print('Accuracy:',nltk.classify.util.accuracy(classifier,testfeats))

classifier.show_most_informative_features()

pos = [classifier.classify(fs) for (fs,l) in posfeats[cutoff:]]
pos = np.array(pos)

neg = [classifier.classify(fs) for (fs,l) in negfeats[cutoff:]]
neg = np.array(neg)

print('Confusion Matrix:')

print('\t'*2,'Predicted Class')
print('-'*40)
print('|\t %d (TP) \t|\t %d (FN) \t| Actual class' %((pos=='pos').sum(),(pos=='neg').sum()))
print('-'*40)
print('|\t %d (FP) \t|\t %d (TN) \t| Actual class' %((neg=='pos').sum(),(neg=='neg').sum()))
print('-'*40)



