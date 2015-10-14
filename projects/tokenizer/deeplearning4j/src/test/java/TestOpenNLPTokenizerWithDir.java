import org.deeplearning4j.text.tokenization.tokenizer.DefaultStreamTokenizer;
import org.deeplearning4j.text.tokenization.tokenizer.DefaultTokenizer;
import org.junit.Before;
import org.junit.Test;
import utils.FileHandler;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.time.Duration;
import java.time.Instant;

/**
 * Created by ruben on 09/07/15.
 */
public class TestOpenNLPTokenizerWithDir {

    private final String TXT_PATH = "/Users/ruben/Desktop/txt";

    @Test
    public void count(){
        int n = 0;
        String[] files = new File(TXT_PATH).list();
        for (String file : files) {
            String content = FileHandler.readFileContent(TXT_PATH + file);
            n += content.split(" ").length;
        }
        System.out.println("total: " + n);
    }

    @Test
    public void testDefaultTokenizerWithDocs() {
        String[] files = new File(TXT_PATH).list();
        DefaultTokenizer defaultTokenizer;
        int total = 0;

        Instant before = Instant.now();
        for (String file : files) {
            String content = FileHandler.readFileContent(TXT_PATH + file);
            defaultTokenizer = new DefaultTokenizer(content);
            total += defaultTokenizer.countTokens();
        }
        System.out.println("Total: " + total + "en " + Duration.between(Instant.now(), before));
    }


    @Test
    public void testDefaultStreamTokenizerWithDocs() throws FileNotFoundException {
        String[] files = new File(TXT_PATH).list();
        DefaultStreamTokenizer defaultStreamTokenizer;
        int total = 0;

        Instant before = Instant.now();
        for (String file : files) {
            InputStream inputStream = new FileInputStream(TXT_PATH + file);
            defaultStreamTokenizer = new DefaultStreamTokenizer(inputStream);
            total += defaultStreamTokenizer.countTokens();
        }
        System.out.println("Total: " + total + "en " + Duration.between(Instant.now(), before));
    }
}
