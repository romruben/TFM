package lc4j;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

/**
 * Created by ruben on 28/06/15.
 */
public class LanguageProfiles {

    private static LanguageProfiles instance;
    private final Properties properties;

    public static LanguageProfiles getInstance(){
        if (instance == null) instance = new LanguageProfiles();
        return instance;
    }

    private LanguageProfiles(){
        properties = new Properties();
        loadProfilePropertiesFile();
    }

    private void loadProfilePropertiesFile() {
        InputStream inputStream = ClassLoader.getSystemResourceAsStream("profiles.properties");
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
