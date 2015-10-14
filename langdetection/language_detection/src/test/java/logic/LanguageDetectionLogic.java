package logic;

import languagedetection.LanguageDetection;
import languagedetection.LanguageProfiles;
import utils.FileHandler;

import java.util.Map;

/**
 * Created by ruben on 30/06/15.
 */
public class LanguageDetectionLogic {

    public static int compareFilesWithLanguageDetected(Map<String, String> filesToTest, LanguageDetection languageDetection) {
        int detected = 0;
        for (String file : filesToTest.keySet()) {
            String langid = languageDetection.detect(FileHandler.readFileContent(file));
            String langName = LanguageProfiles.getInstance().getLanguage(langid);
            if (langName.equalsIgnoreCase(filesToTest.get(file))) detected++;
        }
        return detected;
    }
}
