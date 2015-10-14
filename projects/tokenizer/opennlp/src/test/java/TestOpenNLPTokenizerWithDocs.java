import opennlp.tools.tokenize.Tokenizer;
import opennlp.tools.tokenize.TokenizerME;
import opennlp.tools.tokenize.TokenizerModel;
import org.junit.Before;
import org.junit.Test;
import utils.FileHandler;
import utils.PropertiesProvider;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.time.Duration;
import java.time.Instant;

/**
 * Created by ruben on 09/07/15.
 */
public class TestOpenNLPTokenizerWithDocs {

    private String model;
    private final String TXT_PATH = "/Users/ruben/Desktop/txt/";

    @Before
    public void setUp() {
        model = PropertiesProvider.getInstance().getModelByLang();
    }


    @Test
    public void testWithDocs() throws IOException {
        Instant before = Instant.now();

        InputStream is = new FileInputStream(model);
        TokenizerModel model = new TokenizerModel(is);
        Tokenizer tokenizer = new TokenizerME(model);


        String[] files = new File(TXT_PATH).list();
        int total = 0;

        for (String file : files) {
            String content = FileHandler.readFileContent(TXT_PATH + file);
            total += tokenizer.tokenize(content).length;
        }

        System.out.println("Total: " + total + " in " + Duration.between(Instant.now(), before));
    }
}
