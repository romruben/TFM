package postagger;

import com.aliasi.hmm.HiddenMarkovModel;
import com.aliasi.hmm.HmmDecoder;
import com.aliasi.tag.Tagging;
import com.aliasi.util.Streams;
import utils.FileHandler;

import java.io.*;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

/**
 * Created by ruben on 20/07/15.
 */
public class LingPipePOSTagger {

    private static final String LINGPIPE_BROWN_MODEL = "src/main/resources/pos-en-general-brown.HiddenMarkovModel";
    private static final String DETROIT_PROCESSED_CORPUS   = "src/main/resources/detroit_processed.txt";

    public Tagging<String> tag() {

        HiddenMarkovModel hmm = getModel();
        HmmDecoder decoder = new HmmDecoder(hmm);
        List<String> tokenList = Arrays.asList(FileHandler.readFileContent(DETROIT_PROCESSED_CORPUS)
                .replace("\n","")
                .split(" "));

        return decoder.tag(tokenList);
    }

    private HiddenMarkovModel getModel() {
        try {
            FileInputStream objIn = new FileInputStream(LINGPIPE_BROWN_MODEL);
            ObjectInputStream objectInputStream = new ObjectInputStream(objIn);
            HiddenMarkovModel hiddenMarkovModel = (HiddenMarkovModel) objectInputStream.readObject();
            Streams.closeQuietly(objIn);
            return hiddenMarkovModel;
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
        return null;
    }
}
