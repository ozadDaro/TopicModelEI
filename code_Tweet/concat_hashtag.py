# -*- coding: utf-8 -*-


import gensim
from gensim import corpora
from proj_tweet import *


csv_final = make_csv('2016')
csv_final.to_csv('final.csv')

texts = preprocessing(csv['TEXT'].as_matrix())

hashtag = collect_hashtag(texts)

texts_concat, used = concat_hashtag(texts, hashtag)
save_texts_concat(texts_concat, 'texts_concat.txt')

save_tweets(texts, used, 'tweets_no_hashtag.txt')
