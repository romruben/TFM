import cc.mallet.extract.BIOTokenizationFilter;
import cc.mallet.extract.StringTokenization;
import cc.mallet.extract.Tokenization;
import cc.mallet.extract.TokenizationFilter;
import cc.mallet.extract.pipe.TokenSequence2Tokenization;
import cc.mallet.util.CharSequenceLexer;
import org.junit.Before;
import org.junit.Test;
import utils.FileHandler;
import utils.PropertiesProvider;

import java.time.Duration;
import java.time.Instant;
import java.util.Date;

/**
 * Created by ruben on 09/07/15.
 */
public class TestMalletTokenizer {

    public String fileContent;

    @Before
    public void setUp(){
        fileContent = FileHandler.readFileContent(PropertiesProvider.getInstance().getTestFile());
    }

    @Test
    public void test(){
        Instant before = Instant.now();
        Tokenization tokenization = new StringTokenization(fileContent, new CharSequenceLexer(PropertiesProvider.getInstance().getRegex()));
        System.out.println("Expected 282, Obtained "+ tokenization.size()+ " in "+ Duration.between(Instant.now(), before));
    }
}
