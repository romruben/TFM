package test;

import logic.TestOpenNLPLogic;

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
        testOpenNLPLogic.evaluateCorpusWithModel(PERCEPTRON_MODEL);
    }

    private static void testOpenNLPwithPOSMaxent() {
        testOpenNLPLogic.evaluateCorpusWithModel(MAXENT_MODEL);
    }



}
