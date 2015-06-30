/**
 * Created by ruben on 28/06/15.
 */


import net.olivo.lc4j.LanguageCategorization;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.StringReader;

public class LangDectection {

    LanguageCategorization languageCategorization;

    public LangDectection() {
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

//    public static void main(String[] args) {
//        LangDectection langDectection = new LangDectection();
//        langDectection.detect("hola como estas");
//    }
}