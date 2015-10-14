package lc4j;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

/**
 * Created by ruben on 02/09/15.
 */
public class LanguageProfilesWithEuropaParl {
    private static LanguageProfilesWithEuropaParl instance;
    private final Properties properties;

    public static LanguageProfilesWithEuropaParl getInstance(){
        if (instance == null) instance = new LanguageProfilesWithEuropaParl();
        return instance;
    }

    private LanguageProfilesWithEuropaParl(){
        properties = new Properties();
        loadProfilePropertiesFile();
    }

    private void loadProfilePropertiesFile() {
        InputStream inputStream = ClassLoader.getSystemResourceAsStream("profiles_europaParl.properties");
        try {
            properties.load(inputStream);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String getLanguage(String id){
        return properties.getProperty(id);
    }

}
