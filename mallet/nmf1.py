import os
import numpy as np
import sklearn.feature_extraction.text as text
from sklearn import decomposition




CORPUS_PATH = os.path.join('data', 'austen-brontë-split')


filenames = sorted([os.path.join(CORPUS_PATH, fn) for fn in os.listdir(CORPUS_PATH)])

print(len(filenames))

print(filenames[:5])

vectorizer = text.CountVectorizer(input='filename', stop_words='english', min_df=20)


dtm = vectorizer.fit_transform(filenames).toarray()


vocab = np.array(vectorizer.get_feature_names())

print(dtm.shape)

print(len(vocab))

num_topics = 20
num_top_words = 20


clf = decomposition.NMF(n_components=num_topics, random_state=1)

doctopic = clf.fit_transform(dtm)

topic_words = []

for topic in clf.components_:
	word_idx = np.argsort(topic)[::-1][0:num_top_words]
	topic_words.append([vocab[i] for i in word_idx])
	
	
doctopic = doctopic / np.sum(doctopic, axis=1, keepdims=True)

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
	doctopic_grouped[i, :] = np.mean(doctopic[novel_names == name, :], axis=0)
	
	
doctopic = doctopic_grouped


print(doctopic)

novels = sorted(set(novel_names))
print("Top NMF topics in...")

for i in range(len(doctopic)):
	top_topics = np.argsort(doctopic[i,:])[::-1][0:3]
	top_topics_str = ' '.join(str(t) for t in top_topics)
	print("{}: {}".format(novels[i], top_topics_str))
	
for t in range(len(topic_words)):
	print("Topic {}: {}".format(t, ' '.join(topic_words[t][:15])))
	
	
austen_indices, cbronte_indices = [], []

for index, fn in enumerate(sorted(set(novel_names))):
	if "Austen" in fn:
		austen_indices.append(index)
	elif "CBronte" in fn:
		cbronte_indices.append(index)
		
austen_avg = np.mean(doctopic[austen_indices, :], axis=0)

cbronte_avg = np.mean(doctopic[cbronte_indices, :], axis=0)


keyness = np.abs(austen_avg - cbronte_avg)

ranking = np.argsort(keyness)[::-1]  # from highest to lowest; [::-1] reverses order in Python sequences

ranking[:10]


