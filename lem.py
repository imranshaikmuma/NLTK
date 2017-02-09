#lemmatizing is a similar to stemming
#but it gives some form of synonym to the base word

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("better",pos='a'))

#default pos for lemmatizer is noun

