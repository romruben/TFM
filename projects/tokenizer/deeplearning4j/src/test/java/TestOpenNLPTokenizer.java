import opennlp.tools.tokenize.SimpleTokenizer;
import opennlp.tools.tokenize.Tokenizer;
import opennlp.tools.tokenize.TokenizerME;
import opennlp.tools.tokenize.TokenizerModel;
import org.apache.lucene.analysis.ngram.NGramTokenizer;
import org.apache.uima.analysis_engine.AnalysisEngine;
import org.apache.uima.analysis_engine.impl.PearAnalysisEngineWrapper;
import org.apache.uima.analysis_engine.impl.UimacppAnalysisEngineImpl;
import org.apache.uima.resource.ResourceInitializationException;
import org.deeplearning4j.text.tokenization.tokenizer.*;
import org.deeplearning4j.text.uima.UimaResource;
import org.junit.Before;
import org.junit.Test;
import utils.FileHandler;
import utils.PropertiesProvider;

import java.io.*;
import java.time.Duration;
import java.time.Instant;
import java.util.ArrayList;

/**
 * Created by ruben on 09/07/15.
 */
public class TestOpenNLPTokenizer {

    public String fileContent;

    @Before
    public void setUp() {
        fileContent = FileHandler.readFileContent(PropertiesProvider.getInstance().getTestFile());
    }

    @Test
    public void testDefaultStreamTokenizer() throws IOException, ResourceInitializationException {
        InputStream inputStream = new FileInputStream(PropertiesProvider.getInstance().getTestFile());
        Instant before = Instant.now();
        DefaultStreamTokenizer defaultStreamTokenizer = new DefaultStreamTokenizer(inputStream);
        System.out.println("DefaultStreamTokenizer-> Expected: 282, Obtained: " + defaultStreamTokenizer.countTokens()+" in " + Duration.between(Instant.now(), before));
    }

    @Test
    public void testDefaultTokenizer() {
        Instant before = Instant.now();
        DefaultTokenizer defaultTokenizer = new DefaultTokenizer(fileContent);
        System.out.println("DefaultTokenizer-> Expected: 282, Obtained: " + defaultTokenizer.countTokens()+" in " + Duration.between(Instant.now(), before));
    }

//    @Test
//    public void testNGramTokenizer() throws IOException, ResourceInitializationException {
//        Instant before = Instant.now();
//        NGramTokenizer nGramTokenizer = new NGramTokenizer(new FileReader(PropertiesProvider.getInstance().getTestFile()), 1, 10);
//        System.out.println("NGramTokenizer-> Expected: 282, Obtained: " + nGramTokenize.countTokens()+" in " + Duration.between(Instant.now(), before));
//    }

//    @Test
//    public void testPosUimaTokenizer() throws IOException, ResourceInitializationException {
//        Instant before = Instant.now();
//        PosUimaTokenizer posUimaTokenizer = new PosUimaTokenizer(fileContent, new UimacppAnalysisEngineImpl(), new ArrayList<String>());
//        System.out.println("PosUimaTokenizer-> Expected: 282, Obtained: " + posUimaTokenizer.countTokens()+" in " + Duration.between(Instant.now(), before));
//    }
//
//    @Test
//    public void testUimaTokenizer() throws IOException, ResourceInitializationException {
//        Instant before = Instant.now();
//        UimaTokenizer uimaTokenizer = new UimaTokenizer(fileContent, new UimaResource(new PearAnalysisEngineWrapper()), false);
//        System.out.println("UimaTokenizer-> Expected: 282, Obtained: " + uimaTokenizer.countTokens()+" in " + Duration.between(Instant.now(), before));
//    }

}
