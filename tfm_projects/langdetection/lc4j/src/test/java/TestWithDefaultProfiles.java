import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import utils.FileHandler;

import java.time.Duration;
import java.time.Instant;
import java.util.Arrays;
import java.util.Map;

import static org.junit.Assert.assertEquals;

/**
* Created by ruben on 28/06/15.
*/
public class TestWithDefaultProfiles {

    LangDectection langDectection;

    Map<String, String> filesToTest;

    Instant startTestTime;

    @Before
    public void onStartUp() {
        startTestTime = Instant.now();
        langDectection = new LangDectection();
        filesToTest = PropertiesManager.getInstance().getFilesByLanguage(Arrays.asList("English", "Spanish"));
    }

    @Test
    public void detectLanguagesWithStandardProfiles() {
        int detected = 0;
        for (String file : filesToTest.keySet()) {
            String langid = langDectection.detect(FileHandler.readFileContent(file));
            String langName = LanguageProfiles.getInstance().getLanguage(langid);
            if (langName.equalsIgnoreCase(filesToTest.get(file))) detected++;
        }
        assertEquals(filesToTest.size(), detected);
    }

    @After
    public void onEnd() {
        System.out.printf("Time spend: " + Duration.between(Instant.now(), startTestTime));
    }
}
