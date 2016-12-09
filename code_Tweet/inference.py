# -*- coding: utf-8 -*-


import gensim
from gensim import corpora
from proj_tweet import *

ldamodel = gensim.models.ldamodel.LdaModel.load('saveLdaFINAL_2016')

dictionary= corpora.Dictionary.load('sauvegardeDicTopicsTweetsAgregByHashtags2016_5')

sides_by_month = concat_sides_by_months('2016', 'parties_lists.txt')

topic_parti_dist = topic_parti(sides_by_month, ldamodel, dictionary, 50)

for k in topic_parti_dist.keys():
    fichier_topic_parti(parti_topic_dist, 'side:Gauche')
