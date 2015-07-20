import logic.TestOpenNLPLogic;
import postagger.OpenNLPPostTagger;
import utils.FileHandler;

import javax.xml.bind.SchemaOutputResolver;
import java.text.DecimalFormat;
import java.time.Duration;
import java.time.Instant;
import java.time.Period;
import java.util.Date;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/**
 * Created by ruben on 20/07/15.
 */
public class TestOpenNLP {

    private static final String MAXENT_MODEL = "src/main/resources/en-pos-maxent.bin";
    private static final String PERCEPTRON_MODEL = "src/main/resources/en-pos-perceptron.bin";

    private static TestOpenNLPLogic testOpenNLPLogic;

    public static void main(String[] args) {
        testOpenNLPLogic = new TestOpenNLPLogic();

        testOpenNLPwithPOSMaxent();
        testOpenNLPwithPOSPerceptron();
    }

    private static void testOpenNLPwithPOSPerceptron() {
        testOpenNLPLogic.evaluateCorpusWithModel(PERCEPTRON_MODEL);
    }

    private static void testOpenNLPwithPOSMaxent() {
        testOpenNLPLogic.evaluateCorpusWithModel(MAXENT_MODEL);
    }

}
