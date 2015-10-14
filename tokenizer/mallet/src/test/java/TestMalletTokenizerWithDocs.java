import cc.mallet.extract.StringTokenization;
import cc.mallet.extract.Tokenization;
import cc.mallet.util.CharSequenceLexer;
import org.junit.Test;
import utils.FileHandler;
import utils.PropertiesProvider;

import java.io.File;
import java.time.Duration;
import java.time.Instant;

/**
 * Created by ruben on 09/07/15.
 */
public class TestMalletTokenizerWithDocs {

    private String TXT_PATH = "/Users/ruben/Desktop/txt";

    @Test
    public void testWithDocs() {

        Tokenization tokenization;

        String[] files = new File(TXT_PATH).list();
        Instant before = Instant.now();
        int total = 0;

        for (String file : files) {
            String content = FileHandler.readFileContent(TXT_PATH + file);
            tokenization = new StringTokenization(content, new CharSequenceLexer(PropertiesProvider.getInstance().getRegex()));
            total += tokenization.size();
        }

        System.out.println("Total: " + total + " in " + Duration.between(Instant.now(), before));
    }
}
