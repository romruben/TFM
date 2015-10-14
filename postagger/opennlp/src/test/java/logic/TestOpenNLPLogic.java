package logic;

import utils.FileHandler;

import java.io.File;
import java.text.DecimalFormat;
import java.time.Duration;
import java.time.Instant;
import java.util.HashMap;
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
        OpenNLPPostTagger openNLPPostTagger = new OpenNLPPostTagger(model);

        String[] original_tagged_corpus = getOriginalCorpusTagged(FileHandler.readFileContent(ORIGINAL_CORPUS_FILE).replace("\n", "").split(" "));
        String[] processed_tagged_corpus = openNLPPostTagger.tag(FileHandler.readFileContent(PROCESSED_CORPUS_FILE).replace("\n", "").split(" "));

        int expected = original_tagged_corpus.length;
        int obtained = compareCorpus(original_tagged_corpus, processed_tagged_corpus);

        print_results(before, expected, obtained, model);
    }

    public HashMap<String, Long> evaluateCorpusWithModelWithADir(String model, String dir) {
        OpenNLPPostTagger openNLPPostTagger = new OpenNLPPostTagger(model);
        HashMap<String, Long> results = new HashMap<>();

        long total = 0;
        long detected = 0;

        for (File file : ((new File(dir)).listFiles())) {
            total += FileHandler.readFileContent(file.getAbsolutePath()).replace("\n", "").split(" ").length;
            detected += openNLPPostTagger.tag(FileHandler.readFileContent(file.getAbsolutePath()).replace("\n", "").split(" ")).length;
        }

        results.put("total", total);
        results.put("detected", detected);

        return results;
    }

    public String evaluateCorpusWithModelWithAFile(String model, String file) {
        OpenNLPPostTagger openNLPPostTagger = new OpenNLPPostTagger(model);
        return String.join(" ", openNLPPostTagger.tag(FileHandler.readFileContent(file).replace("\n", "").split(" ")));
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
