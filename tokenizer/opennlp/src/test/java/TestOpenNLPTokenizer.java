import opennlp.tools.tokenize.Tokenizer;
import opennlp.tools.tokenize.TokenizerME;
import opennlp.tools.tokenize.TokenizerModel;
import org.junit.Before;
import org.junit.Test;
import utils.FileHandler;
import utils.PropertiesProvider;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.time.Duration;
import java.time.Instant;

/**
 * Created by ruben on 09/07/15.
 */
public class TestOpenNLPTokenizer {

    private String fileContent;
    private String model;

    @Before
    public void setUp() {
        fileContent = FileHandler.readFileContent(PropertiesProvider.getInstance().getTestFile());
        model = PropertiesProvider.getInstance().getModelByLang();
    }

    @Test
    public void test() throws IOException {
        Instant before = Instant.now();

        InputStream is = new FileInputStream(model);

        TokenizerModel model = new TokenizerModel(is);
        Tokenizer tokenizer = new TokenizerME(model);

        System.out.println("TokenizerMe expected 282, obtained : " + tokenizer.tokenize(fileContent).length +
                " in " + Duration.between(Instant.now(), before));

        is.close();
    }

}
