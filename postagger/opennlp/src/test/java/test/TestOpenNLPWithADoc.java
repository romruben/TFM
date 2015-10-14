package test;

import logic.TestOpenNLPLogic;

import java.time.Duration;
import java.time.Instant;
import java.util.HashMap;

/**
 * Created by ruben on 20/07/15.
 */
public class TestOpenNLPWithADoc {

    private static final String file = "/Users/ruben/Desktop/postaggers.txt";
    private static final String MAXENT_MODEL = "src/main/resources/en-pos-maxent.bin";
    private static final String PERCEPTRON_MODEL = "src/main/resources/en-pos-perceptron.bin";

    private static TestOpenNLPLogic testOpenNLPLogic;

    public static void main(String[] args) {
        testOpenNLPLogic = new TestOpenNLPLogic();

        testOpenNLPwithPOSMaxent();
        testOpenNLPwithPOSPerceptron();
    }

    private static void testOpenNLPwithPOSPerceptron() {
        Instant before = Instant.now();
        String results = testOpenNLPLogic.evaluateCorpusWithModelWithAFile(PERCEPTRON_MODEL, file);
        System.out.println("testOpenNLPwithPOSPerceptron:  in " + Duration.between(before, Instant.now()));
        System.out.println(results);
    }

    private static void testOpenNLPwithPOSMaxent() {
        Instant before = Instant.now();
        String results = testOpenNLPLogic.evaluateCorpusWithModelWithAFile(MAXENT_MODEL, file);
        System.out.println("testOpenNLPwithPOSMaxent:  in " + Duration.between(before, Instant.now()));
        System.out.println(results);
    }

}
