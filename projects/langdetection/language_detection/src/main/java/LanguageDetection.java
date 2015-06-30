/**
 * Created by ruben on 28/06/15.
 */

import java.util.ArrayList;

import com.cybozu.labs.langdetect.Detector;
import com.cybozu.labs.langdetect.DetectorFactory;
import com.cybozu.labs.langdetect.LangDetectException;
import com.cybozu.labs.langdetect.Language;

public class LanguageDetection {
    public void init(String profileDirectory) {
        try {
            DetectorFactory.loadProfile(profileDirectory);
        } catch (LangDetectException e) {
            e.printStackTrace();
        }
    }

    public String detect(String text) {
        Detector detector;
        try {
            detector = DetectorFactory.create();
            detector.append(text);
            return detector.detect();
        } catch (LangDetectException e) {
            e.printStackTrace();
        }
        return "None";
    }

    public ArrayList<Language> detectLangs(String text) throws LangDetectException {
        Detector detector = DetectorFactory.create();
        detector.append(text);
        return detector.getProbabilities();
    }
}