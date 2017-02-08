from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize

text = "This is an example program on stop words"

stop_words = set(stopwords.words("English"))

print(stop_words)

words = word_tokenize(text)

filter = []

for w in words:
	if w not in stop_words:
		filter.append(w)
		
		
print(filter)