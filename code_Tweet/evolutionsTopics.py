# -*- coding: utf-8 -*-
"""
Ce script permet de générer diffèrentes courbes permettant de visualiser
 l'évolution de certains topics au cours de l'année 2016
"""
# encoding=utf8
import sys




reload(sys)
sys.setdefaultencoding('utf8')

#Mapping entre le numéro de topics de LDAvis et de lda de gensim
v = {}
v[34]=0
v[31]=1
v[24]=2
v[47]=3
v[8]=5
v[7]=6
v[16]=7
v[19]=9
v[23]=10
v[36]=11
v[10]=12
v[2]=15
v[4]=18
v[7]=19
v[13]=20
v[3]=21
v[42]=24
v[11]=25
v[25]=29
v[22]=31
v[18]=33
v[12]=34
v[6]=36
v[30]=37
v[17]=38
v[28]=41
v[35]=49

from proj_tweets import *

def graphBrexit(conc, ldamodel, dictionaire )	:
	partiDroite = conc["side:Droite"]
	listProbasDroite = []
	numTopic = v[12]
	for mois in partiDroite :
		mois =unicode(mois, errors='ignore')
		text = preprocessing([mois])[0]
		text = remove_hashtag(text)
		topics = ldamodel[dictionaire.doc2bow(text)]
		trouve=0
		for topic in topics :
			if topic[0]==numTopic :
				listProbasDroite.append(topic[1])
				trouve=1
		if trouve==0 :
			listProbasDroite.append(0)
	partiGauche = conc["side:Gauche"]
	listProbasGauche = []
	for mois in partiGauche :
		mois =unicode(mois, errors='ignore')
		text = preprocessing([mois])[0]
		text = remove_hashtag(text)
		topics = ldamodel[dictionaire.doc2bow(text)]
		trouve=0
		for topic in topics :
			if topic[0]==numTopic :
				listProbasGauche.append(topic[1])
				trouve=1
		if trouve==0 :
			listProbasGauche.append(0)
	partiEDroite = conc["side:Extrême-Droite"]
	listProbasEDroite = []
	for mois in partiEDroite :
		mois =unicode(mois, errors='ignore')
		text = preprocessing([mois])[0]
		text = remove_hashtag(text)
		topics = ldamodel[dictionaire.doc2bow(text)]
		trouve=0
		for topic in topics :
			if topic[0]==numTopic :
				listProbasEDroite.append(topic[1])
				trouve=1
		if trouve==0 :
			listProbasEDroite.append(0)
	partiEGauche = conc["side:Extrême-Gauche"]
	listProbasEGauche = []
	for mois in partiEGauche :
		mois =unicode(mois, errors='ignore')
		text = preprocessing([mois])[0]
		text = remove_hashtag(text)
		topics = ldamodel[dictionaire.doc2bow(text)]
		trouve=0
		for topic in topics :
			if topic[0]==numTopic :
				listProbasEGauche.append(topic[1])
				trouve=1
		if trouve==0 :
			listProbasEGauche.append(0)
	partiEDroite = conc["side:Extrême-Droite"]
	listProbasEDroite = []
	for mois in partiEDroite :
		mois =unicode(mois, errors='ignore')
		text = preprocessing([mois])[0]
		text = remove_hashtag(text)
		topics = ldamodel[dictionaire.doc2bow(text)]
		trouve=0
		for topic in topics :
			if topic[0]==numTopic :
				listProbasEDroite.append(topic[1])
				trouve=1
		if trouve==0 :
			listProbasEDroite.append(0)
	partiCentre = conc["side:Centre"]
	listCentre = []
	for mois in partiCentre :
		mois =unicode(mois, errors='ignore')
		text = preprocessing([mois])[0]
		text = remove_hashtag(text)
		topics = ldamodel[dictionaire.doc2bow(text)]
		trouve=0
		for topic in topics :
			if topic[0]==numTopic :
				listCentre.append(topic[1])
				trouve=1
		if trouve==0 :
			listCentre.append(0)
	fig, ax = plt.subplots()
	ax.plot([1,2,3,4,5,6,7,8,9,10],listProbasGauche, label="Gauche")
	ax.plot([1,2,3,4,5,6,7,8,9,10],listProbasDroite, label="Droite")
	ax.plot([1,2,3,4,5,6,7,8,9,10],listCentre, label="Centre")
	plt.title("Evolution du topic brexit pour la droite, la gauche et le centre")
	legend = ax.legend(loc='upper left', shadow=True)
	#plt.legend([p1, p2, p3], ["Gauche", "Droite", "EtremeDroite"])
	plt.show()

def graphEmploi(conc, ldamodel, dictionaire )	:
	partiDroite = conc["side:Droite"]
	listProbasDroite = []
	numTopic = v[2]
	for mois in partiDroite :
		mois =unicode(mois, errors='ignore')
		text = preprocessing([mois])[0]
		text = remove_hashtag(text)
		topics = ldamodel[dictionaire.doc2bow(text)]
		trouve=0
		for topic in topics :
			if topic[0]==numTopic :
				listProbasDroite.append(topic[1])
				trouve=1
		if trouve==0 :
			listProbasDroite.append(0)
	partiGauche = conc["side:Gauche"]
	listProbasGauche = []
	for mois in partiGauche :
		mois =unicode(mois, errors='ignore')
		text = preprocessing([mois])[0]
		text = remove_hashtag(text)
		topics = ldamodel[dictionaire.doc2bow(text)]
		trouve=0
		for topic in topics :
			if topic[0]==numTopic :
				listProbasGauche.append(topic[1])
				trouve=1
		if trouve==0 :
			listProbasGauche.append(0)
	partiCentre = conc["side:Centre"]
	listCentre = []
	for mois in partiCentre :
		mois =unicode(mois, errors='ignore')
		text = preprocessing([mois])[0]
		text = remove_hashtag(text)
		topics = ldamodel[dictionaire.doc2bow(text)]
		trouve=0
		for topic in topics :
			if topic[0]==numTopic :
				listCentre.append(topic[1])
				trouve=1
		if trouve==0 :
			listCentre.append(0)
	fig, ax = plt.subplots()
	ax.plot([1,2,3,4,5,6,7,8,9,10],listProbasGauche, label="Gauche")
	ax.plot([1,2,3,4,5,6,7,8,9,10],listProbasDroite, label="Droite")
	ax.plot([1,2,3,4,5,6,7,8,9,10],listCentre, label="Centre")
	plt.title("Evolution du topic Emploi et Chômage pour la droite, la gauche et le centre")
	legend = ax.legend(loc='upper left', shadow=True)
	#plt.legend([p1, p2, p3], ["Gauche", "Droite", "EtremeDroite"])
	plt.show()


def graphImmigration(conc, ldamodel, dictionaire )	:
	partiDroite = conc["side:Droite"]
	listProbasDroite = []
	numTopic = v[25]
	for mois in partiDroite :
		mois =unicode(mois, errors='ignore')
		text = preprocessing([mois])[0]
		text = remove_hashtag(text)
		topics = ldamodel[dictionaire.doc2bow(text)]
		trouve=0
		for topic in topics :
			if topic[0]==numTopic :
				listProbasDroite.append(topic[1])
				trouve=1
		if trouve==0 :
			listProbasDroite.append(0)
	partiGauche = conc["side:Gauche"]
	listProbasGauche = []
	for mois in partiGauche :
		mois =unicode(mois, errors='ignore')
		text = preprocessing([mois])[0]
		text = remove_hashtag(text)
		topics = ldamodel[dictionaire.doc2bow(text)]
		trouve=0
		for topic in topics :
			if topic[0]==numTopic :
				listProbasGauche.append(topic[1])
				trouve=1
		if trouve==0 :
			listProbasGauche.append(0)
	partiEDroite = conc["side:Extrême-Droite"]
	listProbasEDroite = []
	for mois in partiEDroite :
		mois =unicode(mois, errors='ignore')
		text = preprocessing([mois])[0]
		text = remove_hashtag(text)
		topics = ldamodel[dictionaire.doc2bow(text)]
		trouve=0
		for topic in topics :
			if topic[0]==numTopic :
				listProbasEDroite.append(topic[1])
				trouve=1
		if trouve==0 :
			listProbasEDroite.append(0)
	partiEGauche = conc["side:Extrême-Gauche"]
	fig, ax = plt.subplots()
	ax.plot([1,2,3,4,5,6,7,8,9,10],listProbasGauche, label="Gauche")
	ax.plot([1,2,3,4,5,6,7,8,9,10],listProbasDroite, label="Droite")
	ax.plot([1,2,3,4,5,6,7,8,9,10],listProbasEDroite, label="Extrême Droite")
	plt.title("Evolution du topic Immigration pour la droite, la gauche et l'Extrême Droite")
	legend = ax.legend(loc='upper left', shadow=True)
	#plt.legend([p1, p2, p3], ["Gauche", "Droite", "EtremeDroite"])
	plt.show()

def graphEvasionFiscale(conc, ldamodel, dictionaire )	:
	partiDroite = conc["side:Droite"]
	listProbasDroite = []
	numTopic = v[35]
	for mois in partiDroite :
		mois =unicode(mois, errors='ignore')
		text = preprocessing([mois])[0]
		text = remove_hashtag(text)
		topics = ldamodel[dictionaire.doc2bow(text)]
		trouve=0
		for topic in topics :
			if topic[0]==numTopic :
				listProbasDroite.append(topic[1])
				trouve=1
		if trouve==0 :
			listProbasDroite.append(0)
	partiGauche = conc["side:Gauche"]
	listProbasGauche = []
	for mois in partiGauche :
		mois =unicode(mois, errors='ignore')
		text = preprocessing([mois])[0]
		text = remove_hashtag(text)
		topics = ldamodel[dictionaire.doc2bow(text)]
		trouve=0
		for topic in topics :
			if topic[0]==numTopic :
				listProbasGauche.append(topic[1])
				trouve=1
		if trouve==0 :
			listProbasGauche.append(0)
	partiCentre = conc["side:Centre"]
	listCentre = []
	for mois in partiCentre :
		mois =unicode(mois, errors='ignore')
		text = preprocessing([mois])[0]
		text = remove_hashtag(text)
		topics = ldamodel[dictionaire.doc2bow(text)]
		trouve=0
		for topic in topics :
			if topic[0]==numTopic :
				listCentre.append(topic[1])
				trouve=1
		if trouve==0 :
			listCentre.append(0)
	fig, ax = plt.subplots()
	#ax.plot([1,2,3,4,5,6,7,8,9,10],listProbasGauche, label="Gauche")
	ax.plot([1,2,3,4,5,6,7,8,9,10],listProbasDroite, label="Droite")
	ax.plot([1,2,3,4,5,6,7,8,9,10],listProbasGauche, label="Gauche")
	ax.plot([1,2,3,4,5,6,7,8,9,10],listCentre, label="Centre")
	plt.title("Evolution du topic Evasion Fiscale pour la droite et le centre")
	legend = ax.legend(loc='upper left', shadow=True)
	#plt.legend([p1, p2, p3], ["Gauche", "Droite", "EtremeDroite"])
	plt.show()

def graphAttentats(conc, ldamodel, dictionaire )	:
	partiDroite = conc["side:Droite"]
	listProbasDroite = []
	numTopic = v[10]
	for mois in partiDroite :
		mois =unicode(mois, errors='ignore')
		text = preprocessing([mois])[0]
		text = remove_hashtag(text)
		topics = ldamodel[dictionaire.doc2bow(text)]
		trouve=0
		for topic in topics :
			if topic[0]==numTopic :
				listProbasDroite.append(topic[1])
				trouve=1
		if trouve==0 :
			listProbasDroite.append(0)
	partiGauche = conc["side:Gauche"]
	listProbasGauche = []
	for mois in partiGauche :
		mois =unicode(mois, errors='ignore')
		text = preprocessing([mois])[0]
		text = remove_hashtag(text)
		topics = ldamodel[dictionaire.doc2bow(text)]
		trouve=0
		for topic in topics :
			if topic[0]==numTopic :
				listProbasGauche.append(topic[1])
				trouve=1
		if trouve==0 :
			listProbasGauche.append(0)
	partiEDroite = conc["side:Extrême-Droite"]
	listProbasEDroite = []
	for mois in partiEDroite :
		mois =unicode(mois, errors='ignore')
		text = preprocessing([mois])[0]
		text = remove_hashtag(text)
		topics = ldamodel[dictionaire.doc2bow(text)]
		trouve=0
		for topic in topics :
			if topic[0]==numTopic :
				listProbasEDroite.append(topic[1])
				trouve=1
		if trouve==0 :
			listProbasEDroite.append(0)

	fig, ax = plt.subplots()
	ax.plot([1,2,3,4,5,6,7,8,9,10],listProbasGauche, label="Gauche")
	ax.plot([1,2,3,4,5,6,7,8,9,10],listProbasDroite, label="Droite")
	ax.plot([1,2,3,4,5,6,7,8,9,10],listProbasEDroite, label="Extrême Droite")
	plt.title("Evolution du topic Attentats")
	legend = ax.legend(loc='upper left', shadow=True)
	#plt.legend([p1, p2, p3], ["Gauche", "Droite", "EtremeDroite"])
	plt.show()

def graphLoiTravail(conc, ldamodel, dictionaire )	:
	partiDroite = conc["side:Droite"]
	listProbasDroite = []
	numTopic = v[4]
	for mois in partiDroite :
		mois =unicode(mois, errors='ignore')
		text = preprocessing([mois])[0]
		text = remove_hashtag(text)
		topics = ldamodel[dictionaire.doc2bow(text)]
		trouve=0
		for topic in topics :
			if topic[0]==numTopic :
				listProbasDroite.append(topic[1])
				trouve=1
		if trouve==0 :
			listProbasDroite.append(0)
	partiGauche = conc["side:Gauche"]
	listProbasGauche = []
	for mois in partiGauche :
		mois =unicode(mois, errors='ignore')
		text = preprocessing([mois])[0]
		text = remove_hashtag(text)
		topics = ldamodel[dictionaire.doc2bow(text)]
		trouve=0
		for topic in topics :
			if topic[0]==numTopic :
				listProbasGauche.append(topic[1])
				trouve=1
		if trouve==0 :
			listProbasGauche.append(0)
	partiEGauche = conc["side:Extrême-Gauche"]
	listProbasEGauche = []
	for mois in partiEGauche :
		mois =unicode(mois, errors='ignore')
		text = preprocessing([mois])[0]
		text = remove_hashtag(text)
		topics = ldamodel[dictionaire.doc2bow(text)]
		trouve=0
		for topic in topics :
			if topic[0]==numTopic :
				listProbasEGauche.append(topic[1])
				trouve=1
		if trouve==0 :
			listProbasEGauche.append(0)
	fig, ax = plt.subplots()
	#ax.plot([1,2,3,4,5,6,7,8,9,10],listProbasGauche, label="Gauche")
	ax.plot([1,2,3,4,5,6,7,8,9,10],listProbasDroite, label="Droite")
	ax.plot([1,2,3,4,5,6,7,8,9,10],listProbasGauche, label="Gauche")
	ax.plot([1,2,3,4,5,6,7,8,9,10],listProbasEGauche, label="Extrême Gauche")
	plt.title("Evolution du topic Loi Travail")
	legend = ax.legend(loc='upper left', shadow=True)
	#plt.legend([p1, p2, p3], ["Gauche", "Droite", "EtremeDroite"])
	plt.show()


ldamodel = gensim.models.ldamodel.LdaModel.load(r'saveLdaFINAL_2016')
print ("lda ok")
dictionary= corpora.Dictionary.load(r'finalDICT')
print ("dic ok")

conc = concat_sides_by_months('D:/Downloads/agg_data/2016/', 'D:/Downloads/parties_lists.txt')
print ("conc ok")
save_object("concObjt.pkl", conc)
print ("save ok")
#a=graphTopics(10, conc, ldamodel, dictionary, "side:Gauche" )


graphEvasionFiscale(conc, ldamodel, dictionary )
graphBrexit(conc, ldamodel, dictionary )
graphTravail(conc, ldamodel, dictionary )
graphImmigration(conc, ldamodel, dictionary )
graphLoiTravail(conc, ldamodel, dictionary )
graphAttentats(conc, ldamodel, dictionary )
