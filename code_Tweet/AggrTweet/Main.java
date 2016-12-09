import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Map.Entry;


public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
			  SearchEngine searchEng = new SearchEngine("text_concat_2016.txt", 136611);
			  //searchEng.saveIndex(new File("index.txt"));
			  searchEng.createPoids();
			  System.out.println("Search Engine");
			  BufferedReader reader= new BufferedReader(new FileReader(new File("tweet_2016.txt")));
			  BufferedWriter w = new BufferedWriter(new FileWriter(new File("correspondances_2016.txt")));
			  String line = reader.readLine();
			  int count = 0;
			  int utile = 0;
			  while(line != null){
				  //System.out.println("ligne" + String.valueOf(count));
				  Entry<Integer, Double> result = searchEng.search(line);
				  if(result != null){
					  //System.out.println(result.getValue());
					  if(result.getValue() > 0.5){
						  	utile ++;
					    	w.write(String.valueOf(count));
					    	w.write("\t");
					    	w.write(String.valueOf(result.getKey()));
					    	w.write("\n");
					    }
				  }
			    count++;
			    line = reader.readLine();
			  }
			  reader.close();
			  w.close();
			  System.out.println(utile);
			}
	}


