import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

#state_union is state of union address of various presidents
#PunktSentenceTokenizer is a unsupervised machine learning sentence tokenizer

train_text = state_union.raw("2005-GWBush.txt")
text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(text)

def process_content():
	try:
		for i in tokenized:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			
			print(tagged)
	
	except Exception as e:
		print(str(e))



process_content()








# POS Tag	Description	Example
# CC	coordinating conjunction	and
# CD	cardinal number	1, third
# DT	determiner	the
# EX	existential there	there is
# FW	foreign word	d’hoevre
# IN	preposition/subordinating conjunction	in, of, like
# JJ	adjective	big
# JJR	adjective, comparative	bigger
# JJS	adjective, superlative	biggest
# LS	list marker	1)
# MD	modal	could, will
# NN	noun, singular or mass	door
# NNS	noun plural	doors
# NNP	proper noun, singular	John
# NNPS	proper noun, plural	Vikings
# PDT	predeterminer	both the boys
# POS	possessive ending	friend‘s
# PRP	personal pronoun	I, he, it
# PRP$	possessive pronoun	my, his
# RB	adverb	however, usually, naturally, here, good
# RBR	adverb, comparative	better
# RBS	adverb, superlative	best
# RP	particle	give up
# TO	to	to go, to him
# UH	interjection	uhhuhhuhh
# VB	verb, base form	take
# VBD	verb, past tense	took
# VBG	verb, gerund/present participle	taking
# VBN	verb, past participle	taken
# VBP	verb, sing. present, non-3d	take
# VBZ	verb, 3rd person sing. present	takes
# WDT	wh-determiner	which
# WP	wh-pronoun	who, what
# WP$	possessive wh-pronoun	whose
# WRB	wh-abverb	where, when