package utils;

/**
 * Created by ruben on 28/06/15.
 */
public class PropertiesProvider {

    private static PropertiesProvider instance;

    private static String TEST_FILE = PropertiesProvider.class.getClassLoader().getResource("example.txt").getPath();
    private String TOKEN_MODEL = PropertiesProvider.class.getClassLoader().getResource("en-token.bin").getPath();

    public static PropertiesProvider getInstance() {
        if (instance == null) instance = new PropertiesProvider();
        return instance;
    }

    private PropertiesProvider() {
        TEST_FILE = mergeDefaultPropsWithMvnArgs(TEST_FILE, System.getProperty("testfile"));
        TOKEN_MODEL = mergeDefaultPropsWithMvnArgs(TOKEN_MODEL, System.getenv("tokenmodel"));
    }

    private String mergeDefaultPropsWithMvnArgs(String byDefault, String mvnArg) {
        return mvnArg != null ? mvnArg : byDefault;
    }

    public String getTestFile() {
        return TEST_FILE;
    }

    public String getModelByLang() {
        return TOKEN_MODEL;
    }
}

