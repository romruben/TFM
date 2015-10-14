package test;

import lc4j.LangDetection;
import logic.Lc4jLogic;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import utils.PropertiesManager;

import java.time.Duration;
import java.time.Instant;
import java.util.Map;

import static org.junit.Assert.assertEquals;

/**
* Created by ruben on 28/06/15.
*/
public class TestWithDefaultProfiles {

    private LangDetection langDetection;
    private Map<String, String> filesToTest;
    private Instant startTestTime;

    @Before
    public void onStartUp() {
        startTestTime = Instant.now();
        langDetection = new LangDetection();
        filesToTest = PropertiesManager.getInstance().getFilesToTets();
    }

    @Test
    public void detectLanguagesWithStandardProfiles() {
        int detected = Lc4jLogic.compareFilesWithLanguageDetected(filesToTest, langDetection);
        assertEquals(filesToTest.size(), detected);
    }

    @After
    public void onEnd() {
        System.out.printf("Time spend: " + Duration.between(Instant.now(), startTestTime));
    }
}
