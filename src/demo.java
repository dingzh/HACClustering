// import java.util.Collection;
import java.util.Map;
import java.util.List;
import java.util.ArrayList;
import java.util.stream.Collectors;
import java.io.Reader;
import java.io.FileReader;
import java.io.StringReader;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.nio.file.*;
import java.nio.charset.Charset;

import edu.stanford.nlp.ling.HasWord;
import edu.stanford.nlp.ling.Sentence;
import edu.stanford.nlp.process.DocumentPreprocessor;
import edu.stanford.nlp.io.RuntimeIOException;

public class demo {
	public static void main(String[] args) {
		Reader reader = new StringReader("Something went wrong!");
		try {
			reader = new FileReader(args[0]);
		} catch(FileNotFoundException e) {
			System.out.println(e.getMessage());		
		}

		//read the document and break into words, collect back to sentences.;
		DocumentPreprocessor dp = new DocumentPreprocessor(reader);
		List<String> sentenceList = new ArrayList<String>();
		for (List<HasWord> sentence : dp) {
   		String sentenceString = Sentence.listToString(sentence);
   		sentenceList.add(sentenceString.toString());
		}

		//output count may output the counting eventually
		Map<String, Long> counts =
    			sentenceList.stream().collect(Collectors.groupingBy(e -> e, Collectors.counting()));
		List<String> writeList = new ArrayList<String>();
	    	counts.forEach((k,v)->writeList.add(k));


		Path file = Paths.get("demo.out");
		try {
			Files.write(file, writeList, Charset.forName("UTF-8"));
		} catch(IOException e) {
			System.out.println(e.getMessage());
		}
	}
}


