# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import gensim
from nltk.corpus import stopwords
import nltk
import os
from gensim import corpora
import re
import math
from nltk.stem import WordNetLemmatizer
import pickle
from nltk.stem.snowball import FrenchStemmer
import matplotlib.pyplot as plt

# Enlève les URL des textes
def remove_urls(text):
    text = re.sub(r"(?:\@|http?\://)\S+", "", text)
    text = re.sub(r"(?:\@|https?\://)\S+", "", text)
    return text

# Enlève les # des textes
def remove_hashtag(X1):
    index_remove = []
    for i in range(len(X1)):
        if X1[i] == '#':
            index_remove.append(i)
    X1 = np.delete(X1, index_remove).tolist()
    return X1

# Crée un seul fichier csv à partir des fichiers csv d'une année
def make_csv(nom_dossier):
    listMois = os.listdir(nom_dossier)
    listCsv = []
    for mois in listMois:
        if os.path.isdir(nom_dossier + '/' + mois):
            listNameCsv = os.listdir(nom_dossier + '/' + mois)
            for doc_csv in listNameCsv:
                csv = pd.read_csv(nom_dossier + '/' + mois + '/' + doc_csv, sep = '\t', quoting = 3)
                listCsv.append(csv)
    csv_final = pd.concat(listCsv)
    return csv_final

# renvoie une liste de documents sous forme d'une liste de mots
# On a effectué une lemmatisation, enlevé les stop words et enlevé les URL
def preprocessing(documents):
    for i in range(len(documents)):
        documents[i] = remove_urls(documents[i])
    ponctuation = ['.', '?', ';', ':', ',', '...', '!','%', '(', ')', '=', '&', '"', '[',']', '>', '<', '\'', '\'\'', '`', '``', ' ', '-', 'ı', '']
    mots_enlever = ['le', 'la', 'je', 'nous', 'c\'est', 'il', 'faut', 'faire']

    stop_words = stopwords.words('french') + stopwords.words('english') + ponctuation + mots_enlever

    #lemmatiser = WordNetLemmatizer()
    stemmer = FrenchStemmer()
    texts = [[stemmer.stem(word.lower()) for word in nltk.word_tokenize(document) if word.lower() not in stop_words] for document in documents]
    return texts

# Crée un dictionnaire avec les hashtag comme clé et la liste des textes contenant ce hashtag en valeur
def collect_hashtag(texts):
    hashtag = {}
    for i in range(len(texts)):
        for j in range(len(texts[i])):
            if texts[i][j] == '#':
                if j + 1 < len(texts[i]):
                    if texts[i][j+1] in hashtag.keys():
                        inter = hashtag[texts[i][j+1]]
                        inter.append(i)
                        hashtag[texts[i][j+1]] = inter
                    else:

                        inter2 = []
                        inter2.append(i)
                        hashtag[texts[i][j+1]] = inter2
    return hashtag


# Effectue la concaténation en fonction des  hashtags
# Used est l'ensemble des indices des tweets contenant un hashtag
def concat_hashtag(texts, hashtag):
    texts_concat = []

    used = set()

    for cle in hashtag.keys():
        inter = sum([texts[c] for c in hashtag[cle]], [])
        texts_concat.append(inter)
        for x in hashtag[cle]:
            used.add(x)
    return (texts_concat, used)

# Enregistre dans un fichier les textes concaténés par hashtag
def save_texts_concat(texts_concat, nom_fichier):
    fichier = open(nom_fichier, 'w')
    for tweet in texts_concat:
        for mot in tweet:
            fichier.write(mot)
            fichier.write('\t')
        fichier.write('\n')
    fichier.close()

    print("number of texts : ",len(texts_concat))

# Enregistre dans un fichier les tweets qui n'ont pas été concaténés
def save_tweets(texts, used, nom_fichier):
    count = 0
    fichier = open(nom_fichier, 'w')
    for i in range(len(texts)):
        if i not in used:
            count += 1
            for mot in texts[i]:
                fichier.write(mot)
                fichier.write('\t')
            fichier.write('\n')
    fichier.close()

    print("number of requests : ",count)

# Charge un fichier comme une liste de liste de mots
def load_text(nom_fichier):
    texts = []
    for line in open(nom_fichier, 'r'):
        texts.append(line.split('\t'))
    return texts


# Crée un dictionnaire avec comme clé le parti et comme valeur la concaténation des tweets de ce parti
def concat_sides(mapping_fichier, csv):
    mapping=pd.read_csv(mapping_fichier, sep = '\t')
    mapping=mapping.as_matrix()
    side={}
    for i in range(mapping.shape[0]) :
        side[mapping[i][1].split(",")[0]]=""
    for i in range(mapping.shape[0]) :
        tweetsMap = csv[csv['SOURCE']==mapping[i][0]]
        for text in tweetsMap["TEXT"]:
            side[mapping[i][1].split(",")[0]]=side[mapping[i][1].split(",")[0]]+ " " + text
    return side

# Amélioration de la méthode précédente qui permet de prendre en compte des tweets avec plusieurs sources
def concat_sides2(mapping, csv):
    side={}
    mapping
    for i in range(mapping.shape[0]) :
        side[mapping[i][1]]=""
    textes = csv['TEXT'].as_matrix()
    print(textes.shape)
    source = csv['SOURCE'].as_matrix()
    for i in range(textes.shape[0]):
        source_split = source[i].split(',')
        for s in source_split:
            for j in range(mapping.shape[0]):
                if mapping[j][0] == s:
                    side[mapping[j][1]] =side[mapping[j][1]] + " " + textes[i]
    return side


# Crée un dictionnaire avec comme clé le parti et comme valeur la liste de la concaténation des tweets de chaque mois
def concat_sides_by_months(nom_dossier, mapping_fichier):
    mapping=pd.read_csv(mapping_fichier, sep = '\t')
    mapping=mapping.as_matrix()
    for i in range(mapping.shape[0]):
        mapping[i][1] = mapping[i][1].split(",")[0]
    listMois = os.listdir(nom_dossier)
    sides_by_month = {}
    for x in mapping[:,1]:
        sides_by_month[x] = []
    print(sides_by_month)
    for mois in listMois:
        listCsv = []
        if os.path.isdir(nom_dossier + '/' + mois):
            listNameCsv = os.listdir(nom_dossier + '/' + mois)
            for doc_csv in listNameCsv:
                csv = pd.read_csv(nom_dossier + '/' + mois + '/' + doc_csv, sep = '\t', quoting = 3)
                listCsv.append(csv)
            csv_mois = pd.concat(listCsv)
            side = concat_sides2(mapping, csv_mois)
            for k in side.keys():
                sides_by_month[k] = sides_by_month[k] + [side[k]]
    return sides_by_month


# Méthode qui permet de sauvegarder un objet en utilisant pickle
def save_object(name, objet):
    with open(name, 'wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(objet)

# Méthode qui permet de charger un objet sauvegardé par la méthode précédente
def load_object(name):
    with open(name, 'rb') as fichier:
        depickler = pickle.Unpickler(fichier)
        object_rec = depickler.load()
        return object_rec

# Affiche un graphique de la proportion du topic numTopic en fonction du temps pour le parti nomParti
def graphTopics(numTopic, conc, ldamodel, dictionaire, nomParti )	:
    parti = conc[nomParti]
    parti = preprocessing(parti)

    listProbas = []
    for mois in parti:
        text = remove_hashtag(mois)
        topics = ldamodel[dictionaire.doc2bow(text)]
        trouve=0
        for topic in topics :
            if topics[0]==numTopic :
                listProbas.append(topics[1])
                trouve=1
            if trouve==0 :
                listProbas.append(0)
    plt.plot(range(10), listProbas)
    plt.show()

# Crée un dictionnaire qui pour chaque parti contient une matrice avec les proportions de chaque topic pour chaque mois.
def topic_parti(conc, ldamodel, dictionnaire, numTopics):
    parti_topic_dist = {}
    for k in conc.keys():
        conc[k] =preprocessing(conc[k])
        topic_dist = np.zeros((10, numTopics))
        for i in range(len(conc[k])):
            text = remove_hashtag(conc[k][i])
            topics = ldamodel.get_document_topics(dictionnaire.doc2bow(text))
            for topic in topics:
                num_topic,proba = topic
                topic_dist[i][num_topic] = proba
        parti_topic_dist[k] = topic_dist
    return parti_topic_dist

# Permet de sauvegarder au format csv la matrice créé dans la fonction précédente pour le parti nomParti
def fichier_topic_parti(parti_topic_dist, nomParti):
    matrice = parti_topic_dist[nomParti]
    np.savetxt(nomParti + ".csv", matrice, delimiter=",")
