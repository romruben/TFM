package lc4j; /**
 * Created by ruben on 28/06/15.
 */


import net.olivo.lc4j.LanguageCategorization;
import utils.PropertiesManager;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.StringReader;

public class LangDetection {

    private LanguageCategorization languageCategorization;

    public LangDetection() {
        try {
            languageCategorization = new LanguageCategorization();
            languageCategorization.loadLanguages(PropertiesManager.getInstance().getProfileDir());
            languageCategorization.setLanguageModelsDir(PropertiesManager.getInstance().getProfileDir());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String detect(String text) {
        return languageCategorization.findLanguage(new BufferedReader(new StringReader(text))).get(0).toString();
    }

}