=======================
INDICATIONS SUR LE CODE
=======================
Le fichier proj_tweet.py contient les m�thodes utilis�es dans concat_hashtag.py, lda.py ainsi que inference.py.

concat_hashtag.py permet � partir du dossier �2016� contenant tous les tweets de cette ann�e de sauvegarder un fichier contenant les tweets agr�g�s par hashtag et un fichier contenant les tweets ne contenant pas de hashtag.

Le dossier agrrTweet contient un programme Java bas� sur le moteur de recherche. Il prend en entr�e les 2 fichiers pr�c�dents et renvoie un fichier avec les textes encore plus agr�g�s que l�on va donner � LDA.

lda.py permet � partir d�un fichier comme celui g�n�r� le programme pr�c�dent de g�n�rer le mod�le LDA et de le sauvegarder

inference.py permet � partir du mod�le LDA et du dictionnaire utilis� par le mod�le de g�n�rer les donn�es sous forme d�un format excel utiles pour afficher les courbes pour chaque parti de la proportion de chapour chaque parti

Le fichier evolutionsTopic.py permet de g�n�rer les graphes qui comparent lՎvolution de la proportion d�un topic en fonction du temps pour chaque parti.

Le fichier visualisation_2016.html est la visualisation pyLDAvis des topics obtenus.