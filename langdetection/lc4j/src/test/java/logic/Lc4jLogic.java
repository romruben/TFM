package logic;

import lc4j.LangDetection;
import lc4j.LanguageProfiles;
import utils.FileHandler;

import java.util.Map;

/**
 * Created by ruben on 30/06/15.
 */
public class Lc4jLogic {

    public static int compareFilesWithLanguageDetected(Map<String, String> filesToTest, LangDetection languageDetection) {
        int detected = 0;
        for (String file : filesToTest.keySet()) {
            String langid = languageDetection.detect(FileHandler.readFileContent(file));
            String langName = LanguageProfiles.getInstance().getLanguage(langid);
            if (langName.equalsIgnoreCase(filesToTest.get(file))) detected++;
        }
        return detected;
    }
}
