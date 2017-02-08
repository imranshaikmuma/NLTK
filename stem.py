#stemming takes out ing and prefix of words and preserve base word
#stemming makes all words in base form and it doesnt affect meaning to analyze text

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

words = ["run","running","ran","runner"]

for w in words:
	print(ps.stem(w))
	
text = "It is import to be pythonly while you are pythoning with python. all pythoners have pythoned poorly atleast once"

text_words =  word_tokenize(text)

for w in text_words:
	print(ps.stem(w))
	

