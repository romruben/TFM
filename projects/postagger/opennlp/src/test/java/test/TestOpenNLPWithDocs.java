package test;

import logic.TestOpenNLPLogic;

import java.time.Duration;
import java.time.Instant;
import java.util.HashMap;

/**
 * Created by ruben on 20/07/15.
 */
public class TestOpenNLPWithDocs {

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
        HashMap<String, Long> results = testOpenNLPLogic.evaluateCorpusWithModelWithADir(PERCEPTRON_MODEL, "/var/tmp/docs/txt");
        System.out.println("total: " + results.get("total") + " detected: " + results.get("detected") + " in " + Duration.between(before, Instant.now()));
    }

    private static void testOpenNLPwithPOSMaxent() {
        Instant before = Instant.now();
        HashMap<String, Long> results = testOpenNLPLogic.evaluateCorpusWithModelWithADir(MAXENT_MODEL, "/var/tmp/docs/txt");
        System.out.println("total: " + results.get("total") + " detected: " + results.get("detected") + " in " + Duration.between(before, Instant.now()));
    }

}
