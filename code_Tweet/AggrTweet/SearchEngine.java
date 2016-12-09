import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Scanner;
import java.util.Map.Entry;
import java.util.SortedSet;
import java.util.TreeMap;
import java.util.TreeSet;


public class SearchEngine {

	private TreeMap<String, TreeMap<Integer, Integer>> index;
	private int documentNumber;
	private static int LIMITE = 100000;
	private double[] docPoids;

	static <K,V extends Comparable<? super V>>
	SortedSet<Map.Entry<K,V>> entriesSortedByValues(Map<K,V> map) {
	    SortedSet<Map.Entry<K,V>> sortedEntries = new TreeSet<Map.Entry<K,V>>(
	        new Comparator<Map.Entry<K,V>>() {
	            @Override public int compare(Map.Entry<K,V> e1, Map.Entry<K,V> e2) {
	                int res = -e1.getValue().compareTo(e2.getValue());
	                return res != 0 ? res : 1;
	            }
	        }
	    );
	    sortedEntries.addAll(map.entrySet());
	    return sortedEntries;
	}

	/**
	 * Crée un engin de recherche depuis les fichiers du dossier dir.
	 * @param dir	Le dossier des documents
	 * @param normalizer	le normalizer
	 * @throws IOException
	 */
	public SearchEngine(String texts,int documentNumber) throws IOException {

		this.index = makeIndex(texts);
		this.documentNumber = documentNumber;
	}

	/**
	 * Crée un engin de recherche à partir du fichier index
	 * @param index
	 * @throws IOException
	 */
	private SearchEngine(File index) throws IOException {
		this.loadIndex(index);
	}

	/**
	 * Renvoie un engin de recherche à partir du fichier index.
	 * @param index
	 * @return un searchEngine
	 * @throws IOException
	 */
	public static SearchEngine loadSearchEngine(File index, int documentNumber) throws IOException {
		SearchEngine se = new SearchEngine(index);
		se.documentNumber = documentNumber;
		return se;
	}


	/**
	 * Crée l'index à partir des fichiers dans le dossier dir
	 * @param dir
	 * @param normalizer
	 * @return
	 * @throws IOException
	 */
	 public static TreeMap<String, TreeMap<Integer, Integer>> makeIndex(String texts) throws IOException{
 		TreeMap<String, TreeMap<Integer, Integer>> invertedFile = new TreeMap<String, TreeMap<Integer, Integer>>();
 		BufferedReader reader = new BufferedReader(new FileReader(new File(texts)));
 		String line = reader.readLine();
		int count = 0;
 		while (line != null){
 			String[] words = line.split("\t");
 			for(String w : words){
 				TreeMap<Integer, Integer> treeMap = invertedFile.get(w);
 				if (treeMap == null){
 					TreeMap<Integer, Integer> init = new TreeMap<Integer,Integer>();
 					init.put(count, 1);
 					invertedFile.put(w, init);
 				}else{
 					Integer res = treeMap.get(count);
 					if(res == null){
						treeMap.put(count, 1);
					}else{
						treeMap.put(count, res + 1);
					}
					invertedFile.put(w, treeMap);
				}
			}
 			line = reader.readLine();
 			count++;
		}
		return invertedFile;

	 }

	 public void createPoids(){
		 double[] docPoidsCarre = new double[documentNumber];
	        for (String s:index.keySet()){
	        	for(int docId:index.get(s).keySet()){
	        		double dfValue = index.get(s).size();
	    			docPoidsCarre[docId] += Math.pow(((double) index.get(s).get(docId)) * Math.log(((double) documentNumber)/ ((double) dfValue)), 2);
	        	}
	        }
	        this.docPoids = docPoidsCarre;
	    }




	/**
	 * Sauvegarde l'index dans un fichier.
	 * Format:
	 * 1ere ligne: nombre de documents
	 * Ensuite: Mot \t nombre de documents qui le contiennent \t document;nombre d'occurence en csv
	 * @param outFile
	 * @throws IOException
	 */
	public void saveIndex(File outFile) throws IOException {
       try {
    	   BufferedWriter writer = new BufferedWriter(new FileWriter(outFile));
    	   writer.write(documentNumber + "\n");
    	   for(String word:index.keySet()){
    		   String writing = word +"\t";
    		   Iterator<Integer> i = index.get(word).keySet().iterator();
    		   while(i.hasNext()){
    			   String mot = String.valueOf(i.next());
    			   writing += mot + ";"+index.get(word).get(mot);
    			   if(i.hasNext()){
    				   writing += ",";
    			   }
    		   }
	    	   writer.write(writing + "\n");
    	   }
    	   writer.close();
	   } catch (IOException e) {
    	   e.printStackTrace();
	   }
	}

	/**
	 * Charge l'index depuis un fichier
	 * @param inFile
	 * @throws IOException
	 */
	private void loadIndex(File inFile) throws IOException {
       try {
    	   BufferedReader reader = new BufferedReader(new FileReader(inFile));
    	   index = new TreeMap<String, TreeMap<Integer, Integer>>();

    	   this.documentNumber = Integer.parseInt(reader.readLine());
    	   String line;
    	   while((line = reader.readLine()) != null) {
    		   String token[] = line.split("\t"); // 0 = mot, 1 = documents

    		   String documents[] = token[1].split(",");
    		   TreeMap<Integer, Integer> docMap = new TreeMap<Integer, Integer>();
    		   for(String doc:documents){
    			   String splitDoc[] = doc.split(";");
    			   docMap.put(Integer.parseInt(splitDoc[0]), Integer.parseInt(splitDoc[1]));
    		   }
    		   index.put(token[0], docMap);
    	   }
    	   reader.close();
	   } catch (IOException e) {
    	   e.printStackTrace();
	   }
	}

	/**
	 * Une méthode renvoyant le nombre d'occurrences
	 * de chaque mot dans un texte.
	 */
	public HashMap<String, Integer>  getTermFrequencies(String texte) {
		// Création de la table des mots
		HashMap<String, Integer> hits = new HashMap<String, Integer>();

		// Appel de la méthode de normalisation
		String[] words = texte.split("\t");
		Integer number;
		// Pour chaque mot de la liste, on remplit un dictionnaire
		// du nombre d'occurrences pour ce mot
		for (String word : words) {
			//word = word.toLowerCase();
			// on récupère le nombre d'occurrences pour ce mot
			// Si ce mot n'était pas encore présent dans le dictionnaire,
			// on l'ajoute (nombre d'occurrences = 1)
			// Sinon, on incrémente le nombre d'occurrence
			number = hits.get(word);
			if(number != null){
				hits.put(word, number+1);
			} else {
				hits.put(word, 1);
			}
		}
		return hits;
	}

	/**
	 * A partir d'une requete (une suite de mots), on cherche les documents les plus pertinents.
	 * @param requete
	 * @return la liste des documents renvoyés.
	 */
	public Entry<Integer, Double> search(String requete){
		// On calcule le tf idf de la requête.
		HashMap<String, Integer> tf;
		HashMap<String, Double> tfidf = new HashMap<String, Double>();
		tf = getTermFrequencies(requete);

		for(String word:tf.keySet()){
			// Si le mot est dans l'index
			if(index.get(word) != null){
				tfidf.put(word, tf.get(word) * Math.log((double)documentNumber / (1.0 + (double)index.get(word).size())));
			}//TODO: si le mot est pas dans l'index faudrait chercher le mot le plus proche si on a le temps
			/**
			 * else {
			 *  Chercher le mot le plus proche
			 * }
			 */
		}
		//System.out.println("doc Number : " + documentNumber);
		// On calcule la similarité entre la requête et les documents qui contiennent au moins un des mots de la requête.
		double poidsRequete = 0.0;
		for (double val : tfidf.values()){
			poidsRequete += val*val;
		}
		poidsRequete = Math.sqrt(poidsRequete);
		HashMap<Integer, Double> similarite = new HashMap<Integer, Double>();

		for(String word:tfidf.keySet()){

			TreeMap<Integer, Integer> ligne = index.get(word);
			for (Integer fichier:ligne.keySet())
			{ Integer tfFichier = ligne.get(fichier) ;
			//System.out.println("tfFichier : " + tfFichier);
			Double simFich = similarite.get(fichier) ;
			//System.out.println("simFich : " + simFich);
				if (simFich==null)
				{
					similarite.put(fichier, tfidf.get(word)*tfFichier*Math.log((double)documentNumber/(1.0+(double)ligne.size()))/(poidsRequete * Math.sqrt(docPoids[fichier]))) ;

				}
				else

				{
					similarite.put(fichier, simFich+tfidf.get(word)*tfFichier*Math.log((double)documentNumber/(1.0+(double)ligne.size()))/(poidsRequete * Math.sqrt(docPoids[fichier]))) ;

				}

			}

		}

		// On renvoie les documents par ordre décroissant de la similarité

		SortedSet<Entry<Integer, Double>> sortedMap = entriesSortedByValues(similarite);
		if (sortedMap.isEmpty()){
			return null;
		}else{
			return sortedMap.first();
		}
	}

}
