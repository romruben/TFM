import java.io.FileInputStream;
import java.io.IOException;
import java.util.*;

/**
 * Created by ruben on 28/06/15.
 */
public class PropertiesManager {

    private static PropertiesManager instance;

    private static String PROFILE_DIR = "/var/tmp/tfm/language_detection/frameworks/languagedetection/profiles/";
    private static String PROFILE_SM_DIR = "/var/tmp/tfm/language_detection/frameworks/languagedetection/profiles.sm/";
    private static String TEST_FILES_DIR = "/var/tmp/tfm/language_detection/frameworks/languagedetection/testfiles/";
    private static String LANGUAGES_TO_TEST = "English,Spanish";
    private static String FILES_BY_LANGUAGE = "src/test/resources/filesByLanguage.properties";

    private static Properties filesByLanguagePropertiesProvider;


    public static PropertiesManager getInstance() {
        if (instance == null) instance = new PropertiesManager();
        return instance;
    }

    private PropertiesManager() {
        PROFILE_DIR = mergeDefaultPropsWithMvnArgs(PROFILE_DIR, System.getProperty("profile.dir"));
        PROFILE_SM_DIR = mergeDefaultPropsWithMvnArgs(PROFILE_SM_DIR, System.getProperty("profile.sm.dir"));
        TEST_FILES_DIR = mergeDefaultPropsWithMvnArgs(TEST_FILES_DIR, System.getProperty("test.dir"));
        loadFilesByLanguageProperties();
    }

    private void loadFilesByLanguageProperties() {
        try {
            filesByLanguagePropertiesProvider = new Properties();
            filesByLanguagePropertiesProvider.load(new FileInputStream(FILES_BY_LANGUAGE));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private String mergeDefaultPropsWithMvnArgs(String byDefault, String mvnArg) {
        return mvnArg != null ? mvnArg : byDefault;
    }

    public String getProfileDir() {
        return PROFILE_DIR;
    }

    public String getProfileSmDir() {
        return PROFILE_SM_DIR;
    }

    public String getTestFilesDir() {
        return TEST_FILES_DIR;
    }

    public List<String> getSupportedLanguages() {
        LANGUAGES_TO_TEST = mergeDefaultPropsWithMvnArgs(LANGUAGES_TO_TEST, System.getProperty("supported.languages"));
        return (new ArrayList(Arrays.asList(LANGUAGES_TO_TEST.split(","))));
    }
    public Map<String, String> getFilesByLanguage(List<String> filter) {
        Map<String, String> filesSupported = toHashMap(filesByLanguagePropertiesProvider);
        filesSupported.values().removeIf(s -> !filter.contains(s));
        return filesSupported;
    }

    public Map<String, String> toHashMap(Properties prop) {
        Map<String, String> map = new HashMap<>();
        prop.stringPropertyNames().forEach(name -> map.put(TEST_FILES_DIR+name, prop.getProperty(name)));
        return map;
    }
}
