package logic;

import postagger.OpenNLPPostTagger;
import utils.FileHandler;

import java.text.DecimalFormat;
import java.time.Duration;
import java.time.Instant;
import java.util.stream.IntStream;

/**
 * Created by ruben on 20/07/15.
 */
public class TestOpenNLPLogic {

    private static final String ORIGINAL_CORPUS_FILE = "src/main/resources/detroit.txt";
    private static final String PROCESSED_CORPUS_FILE = "src/main/resources/detroit_processed.txt";

    public TestOpenNLPLogic() {

    }

    public void evaluateCorpusWithModel(String model) {
        Instant before = Instant.now();
        OpenNLPPostTagger openNLPPostTagger = new OpenNLPPostTagger();

        String[] original_tagged_corpus = getOriginalCorpusTagged(FileHandler.readFileContent(ORIGINAL_CORPUS_FILE).split(" "));
        String[] processed_tagged_corpus = openNLPPostTagger.tag(FileHandler.readFileContent(PROCESSED_CORPUS_FILE).split(" "),
                model);

        int expected = original_tagged_corpus.length;
        int obtained = compareCorpus(original_tagged_corpus, processed_tagged_corpus);

        print_results(before, expected, obtained, model);
    }

    private String[] getOriginalCorpusTagged(String[] original_corpus) {
        String[] tagged = new String[original_corpus.length];
        IntStream.range(0, tagged.length - 1).forEach(i -> tagged[i] = original_corpus[i].split("_")[1]);
        return tagged;
    }

    private int compareCorpus(String[] original_corpus, String[] processed_corpus) {
        int obtained = 0;
        for (int i = 0; i < original_corpus.length - 1; i++) {
            if (original_corpus[i].equalsIgnoreCase(processed_corpus[i])) {
                obtained += 1;
            }
        }
        return obtained;
    }

    private void print_results(Instant before, int expected, int obtained, String model) {
        System.out.print("test OpenNLP, Model: " + model + ", Duration: " + Duration.between(Instant.now(), before) +
                ", Expected: " + expected + ", Obtained: " + obtained + ", Accurancy: " +
                new DecimalFormat("#.##").format((obtained / (double) expected) * 100) + " %\n");
    }

}
