import os
import numpy as np
import itertools
import operator
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt


CORPUS_PATH = os.path.join('data','austen-brontë-split')
filenames = sorted([os.path.join(CORPUS_PATH, fn) for fn in os.listdir(CORPUS_PATH)])

def grouper(n, iterable, fillvalue=None):
	print(iterable)
	args = [iter(iterable)]*n
	return itertools.zip_longest(*args, fillvalue=fillvalue)
	
doctopic_triples = []

mallet_docnames = []

novel_names = []

with open("data\doc-topics.txt") as f:
	f.readline()
	for line in f:
		docnum, docname, *values = line.rstrip().split('\t')
		docname = os.path.basename(docname)
		mallet_docnames.append(docname)
		for topic, share in grouper(2, values):
			triple = (docname,int(topic), float(share))
			doctopic_triples.append(triple)
			

			
doctopic_triples = sorted(doctopic_triples, key=operator.itemgetter(0,1))

mallet_docnames = sorted(mallet_docnames)

num_docs = len(mallet_docnames)
print(num_docs)

print('len of doctopic triples',len(doctopic_triples))
print('len of mallet documents',len(mallet_docnames))
num_topics = len(doctopic_triples) // len(mallet_docnames)
print(num_topics)

doctopic = np.zeros((num_docs, num_topics))
for i, (doc_name, triples) in enumerate(itertools.groupby(doctopic_triples, key=operator.itemgetter(0))):
	doctopic[i, :] = np.array([share for _, _, share in triples])
	
	
novel_names = []

for fn in filenames:
	basename = os.path.basename(fn)
	name, ext = os.path.splitext(basename)
	name = name.rstrip('0123456789')
	novel_names.append(name)
	
novel_names = np.asarray(novel_names)

doctopic_orig = doctopic.copy()

num_groups = len(set(novel_names))

doctopic_grouped = np.zeros((num_groups, num_topics))

for i, name in enumerate(sorted(set(novel_names))):
	doctopic_grouped[i, :] = np.mean(doctopic[novel_names == name, :],axis=0)
	
	
	
doctopic = doctopic_grouped
#print(doctopic)

#print(num_topics)

CORPUS_PATH_UNSPLIT = os.path.join('data','austen-brontë-split')

filenames = [os.path.join(CORPUS_PATH_UNSPLIT, fn) for fn in sorted(os.listdir(CORPUS_PATH_UNSPLIT))]

vectorizer = CountVectorizer(input='filename')

dtm = vectorizer.fit_transform(filenames)  # a sparse matrix

print(dtm.shape)


print(dtm.data.nbytes)  # number of bytes dtm takes up

dtm.toarray().data.nbytes  # number of bytes dtm as array takes up

print(doctopic_orig.shape)

print(doctopic_orig.data.nbytes)  # number of bytes document-topic shares take up


docnames = sorted(set(novel_names))
print(docnames)
print("Top topics in...")

for i in range(len(doctopic)):
	top_topics = np.argsort(doctopic[i,:])[::-1][0:3]
	top_topics_str = ' '.join(str(t) for t in top_topics)
	print("{}: {}".format(docnames[i], top_topics_str))
	


	
with open(r'data\topic-keys.txt') as input:
	topic_keys_lines = input.readlines()
	
topic_words = []

for line in topic_keys_lines:
	_, _, words = line.split('\t')  # tab-separated
	words = words.rstrip().split(' ')  # remove the trailing '\n'
	topic_words.append(words)
	
	
print('words in topic',topic_words[0])


N_WORDS_DISPLAY = 10

for t in range(len(topic_words)):
	print("Topic {}: {}".format(t, ' '.join(topic_words[t][:N_WORDS_DISPLAY])))
	
	
print(docnames)
print(doctopic.shape)
print(doctopic)

N, K = doctopic.shape

ind = np.arange(N)  # points on the x-axis

width = 0.5

plt.bar(ind, doctopic[:,0], width=width)

plt.xticks(ind + width/2, docnames)  # put labels in the center

plt.title('Share of Topic #0')

plt.show()

plots = []


height_cumulative = np.zeros(N)

for k in range(K):
	color = plt.cm.coolwarm(k/K, 1)
	if k == 0:
		p = plt.bar(ind, doctopic[:, k], width, color=color)
	else:
		p = plt.bar(ind, doctopic[:, k], width, bottom=height_cumulative, color=color)
	height_cumulative += doctopic[:, k]
	plots.append(p)

	
plt.ylim((0, 1))

plt.ylabel('Topics')

plt.title('Topics in novels')

plt.xticks(ind+width/2, docnames)

plt.yticks(np.arange(0, 1, 10))

topic_labels = ['Topic #{}'.format(k) for k in range(K)]

plt.legend([p[0] for p in plots], topic_labels)

plt.show()

