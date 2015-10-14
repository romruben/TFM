package test;

import postagger.LingPipePOSTagger;

import java.time.Duration;
import java.time.Instant;

/**
 * Created by ruben on 20/07/15.
 */
public class LingPipeTestsWithADoc {

    public static void main(String[] args) {

        Instant before = Instant.now();
        evaluateLingPipe();
        System.out.println("HiddenMarkovModel  in " + Duration.between(Instant.now(), before));
    }

    private static void evaluateLingPipe() {
        String file = "/Users/ruben/Desktop/postaggers.txt";
        LingPipePOSTagger lingPipePOSTagger = new LingPipePOSTagger();
        System.out.println(lingPipePOSTagger.tag(file));
    }
}
