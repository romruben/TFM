package test;

import com.aliasi.tag.Tagging;
import postagger.LingPipePOSTagger;
import utils.FileHandler;

import java.io.File;
import java.text.DecimalFormat;
import java.time.Duration;
import java.time.Instant;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

import static java.util.stream.Collectors.toList;


/**
 * Created by ruben on 20/07/15.
 */
public class LingPipeTestsWithDocs {

    private static final String DETROIT_ORIGINAL_CORPUS = "src/main/resources/detroit.txt";

    private static long totalTagged = 0;
    private static long totalTokens = 0;

    public static void main(String[] args) {

        Instant before = Instant.now();
        evaluateLingPipe();
        System.out.println("HiddenMarkovModel test, expected: " + totalTokens + " obtained: " + totalTagged + " in " + Duration.between(Instant.now(), before));
    }

    private static void evaluateLingPipe() {
        List<String> files = Stream.of((new File("/var/tmp/docs/txt/")).listFiles()).map(File::getAbsolutePath).collect(toList());
        LingPipePOSTagger lingPipePOSTagger = new LingPipePOSTagger();

        files.forEach(file -> {
            totalTagged += lingPipePOSTagger.tag(file).size();
            totalTokens += Arrays.asList(FileHandler.readFileContent(file).replace("\n", "").split(" ")).size();
        });
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
