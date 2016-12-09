# -*- coding: utf-8 -*-


from proj_tweet import *
import gensim
from gensim import corpora

texts = load_text('texts_final.txt')

dictionary = corpora.Dictionary(texts)

corpus = [dictionary.doc2bow(text) for text in texts]

print('corpus done')

ldamodel = gensim.models.ldamulticore.LdaMulticore(corpus, num_topics=50, id2word = dictionary, passes=40, alpha = 0.01)
ldamodel.save('saveLda')
