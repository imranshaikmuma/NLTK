#corpora is not navigatable
#it is not downlodable individually

import nltk

#print(nltk.__file__) - this is to get packages path in the computer
# to locate the corpora file in the system::::::::::::::
# go to the site packages of nltk and find the data.py and open and see the environment location
# here it is appdata . so go to windows and type %appdata% then it takes you to roaming
# go to nltk_data and find corpora there


from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

text = gutenberg.raw("bible-kjv.txt")
tokens = sent_tokenize(text)

print(tokens)

