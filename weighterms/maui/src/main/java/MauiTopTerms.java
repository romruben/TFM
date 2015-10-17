import com.entopix.maui.filters.MauiFilter;
import com.entopix.maui.main.MauiModelBuilder;
import com.entopix.maui.main.MauiTopicExtractor;
import com.entopix.maui.stemmers.LovinsStemmer;
import com.entopix.maui.stemmers.Stemmer;
import com.entopix.maui.stopwords.Stopwords;
import com.entopix.maui.stopwords.StopwordsSpanish;
import com.entopix.maui.util.DataLoader;
import com.entopix.maui.util.MauiDocument;

import java.util.List;

/**
 * Created by ruben on 14/09/15.
 */
public class MauiTopTerms {

    public static MauiTopicExtractor topicExtractor = new MauiTopicExtractor();
    public static MauiModelBuilder mauiModelBuilder = new MauiModelBuilder();

    /**
     * Sets general parameters: debugging printout, language specific options
     * like stemmer, stopwords.
     *
     * @throws Exception
     */
    private static void setGeneralOptions() {

		/* language specific options*/
        Stemmer stemmer = new LovinsStemmer();
        Stopwords stopwords = new StopwordsSpanish();
        String language = "es";
        String encoding = "UTF-8";
        mauiModelBuilder.stemmer = stemmer;
        mauiModelBuilder.stopwords = stopwords;
        mauiModelBuilder.documentLanguage = language;
        mauiModelBuilder.documentEncoding = encoding;
        topicExtractor.stemmer = stemmer;
        topicExtractor.stopwords = stopwords;
        topicExtractor.documentLanguage = language;


        //specificity options
        mauiModelBuilder.minPhraseLength = 1;
        mauiModelBuilder.maxPhraseLength = 5;


    }

    /**
     * Set which features to use
     */
    private static void setFeatures() {
        mauiModelBuilder.setBasicFeatures(true);
        mauiModelBuilder.setKeyphrasenessFeature(true);
        mauiModelBuilder.setFrequencyFeatures(true);
        mauiModelBuilder.setPositionsFeatures(true);
        mauiModelBuilder.setLengthFeature(true);
        mauiModelBuilder.setThesaurusFeatures(true);
    }

    public static void main(String[] args) throws Exception {

        setGeneralOptions();
        setFeatures();

        // Directories with train & test data
        String trainDir = "src/main/resources/train";
        String testDir = "/Users/ruben/Desktop/_test";

        // name of the file to save the model
        String modelName = "src/main/resources/test_tagging_model";

        // Settings for the model builder
        mauiModelBuilder.inputDirectoryName = trainDir;
        mauiModelBuilder.modelName = modelName;

        // change to 1 for short documents
        mauiModelBuilder.minNumOccur = 2;

        // Run model builder
        List<MauiDocument> trainingDocs = DataLoader.loadTestDocuments(trainDir);
        MauiFilter mauiFilter = mauiModelBuilder.buildModel(trainingDocs);
        mauiModelBuilder.saveModel(mauiFilter);

        // Settings for topic extractor
        topicExtractor.inputDirectoryName = testDir;
        topicExtractor.modelName = modelName;
        topicExtractor.setTopicProbability(0.0);

        // Run topic extractor
        topicExtractor.loadModel();
        List<MauiDocument> testDocs = DataLoader.loadTestDocuments(testDir);
        topicExtractor.extractTopics(testDocs);

    }

}
