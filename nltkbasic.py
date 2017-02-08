import nltk

#nltk.download()
# tokenizer are of two types:
# word tokenizer
# sentence tokenizer

# corpora - a body of text eg: speeches etc

# lexicon  is a dictionary containing word and meanings

from nltk.tokenize import sent_tokenize, word_tokenize

text = "hello imran, what are you doing? Today weather is great. Today is Wednesday."

print(sent_tokenize(text)) 
print(word_tokenize(text))

for i in word_tokenize(text):
	print(i)

	