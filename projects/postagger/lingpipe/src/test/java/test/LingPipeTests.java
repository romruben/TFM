package test;

import com.aliasi.tag.Tagging;
import postagger.LingPipePOSTagger;
import utils.FileHandler;

import java.text.DecimalFormat;
import java.time.Duration;
import java.time.Instant;
import java.util.Arrays;
import java.util.List;

/**
 * Created by ruben on 20/07/15.
 */
public class LingPipeTests {

    private static final String DETROIT_ORIGINAL_CORPUS = "src/main/resources/detroit.txt";

    public static void main(String[] args) {
        evaluateLingPipe();
    }

    private static void evaluateLingPipe() {
        Instant before = Instant.now();


        Tagging<String> processed_tagged_corpus = (new LingPipePOSTagger()).tag();
        List<String> original_tagged_corpus = Arrays.asList(FileHandler.readFileContent(DETROIT_ORIGINAL_CORPUS).replace("\n", "").split(" "));

        int expected = original_tagged_corpus.size();
        int obtained = compareCorpus(original_tagged_corpus, processed_tagged_corpus);

        print_results(before, expected, obtained, "HiddenMarkovModel");
    }

    private static int compareCorpus(List<String> original_tagged_corpus, Tagging<String> processed_tagged_corpus) {
        int total = 0;
        for (int i = 0; i < original_tagged_corpus.size() - 1; i++) {
            if (original_tagged_corpus.get(i).split("_")[1].equalsIgnoreCase(processed_tagged_corpus.tag(i))) {
                total++;
            }
        }
        return total;
    }

    private static void print_results(Instant before, int expected, int obtained, String model) {
        System.out.print("test LingPipeTests, Model: " + model + ", Duration: " + Duration.between(Instant.now(), before) +
                ", Expected: " + expected + ", Obtained: " + obtained + ", Accurancy: " +
                new DecimalFormat("#.##").format((obtained / (double) expected) * 100) + " %\n");
    }
}
