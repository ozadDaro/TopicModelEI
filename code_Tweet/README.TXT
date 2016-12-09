=======================
INDICATIONS SUR LE CODE
=======================
Le fichier proj_tweet.py contient les méthodes utilisées dans concat_hashtag.py, lda.py ainsi que inference.py.

concat_hashtag.py permet à partir du dossier ’2016’ contenant tous les tweets de cette année de sauvegarder un fichier contenant les tweets agrégés par hashtag et un fichier contenant les tweets ne contenant pas de hashtag.

Le dossier agrrTweet contient un programme Java basé sur le moteur de recherche. Il prend en entrée les 2 fichiers précédents et renvoie un fichier avec les textes encore plus agrégés que l’on va donner à LDA.

lda.py permet à partir d’un fichier comme celui généré le programme précédent de générer le modèle LDA et de le sauvegarder

inference.py permet à partir du modèle LDA et du dictionnaire utilisé par le modèle de générer les données sous forme d’un format excel utiles pour afficher les courbes pour chaque parti de la proportion de chapour chaque parti

Le fichier evolutionsTopic.py permet de générer les graphes qui comparent l’évolution de la proportion d’un topic en fonction du temps pour chaque parti.

Le fichier visualisation_2016.html est la visualisation pyLDAvis des topics obtenus.