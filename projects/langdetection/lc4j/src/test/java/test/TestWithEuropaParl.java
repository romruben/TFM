package test;

import lc4j.LangDetection;
import lc4j.LanguageProfilesWithEuropaParl;
import utils.FileHandler;

import java.io.File;
import java.time.Duration;
import java.time.Instant;
import java.util.Objects;

/**
 * Created by ruben on 02/09/15.
 */
public class TestWithEuropaParl {

    static private LangDetection langDetection;

    public static void main(String[] args) {
        Instant before = Instant.now();

        langDetection = new LangDetection();
        File filesdir = new File("/Users/ruben/Desktop/lang");

        int total = getFilesCount(filesdir);
        int welldetected = getFilesWellDetected(filesdir.listFiles());

        System.out.println("total: " + total + " well detected: " + welldetected + " in " + Duration.between(before, Instant.now()));
    }

    private static int getFilesWellDetected(File[] allLangsDir) {
        int detected = 0;

        for (File langdir : allLangsDir){
            if(!langdir.getName().equals(".DS_Store"))
                detected += analyzeLangDir(langdir);
        }

        return detected;
    }

    private static int analyzeLangDir(File langdir) {
        String langName = langdir.getName();
        int docWellDetected = 0;

        for(File file : langdir.listFiles()){
            String detected = LanguageProfilesWithEuropaParl.getInstance().getLanguage(langDetection.detect(FileHandler.readFileContent(file.getAbsolutePath())));

            if (detected != null && !detected.isEmpty() && detected.equals(langName))
                docWellDetected++;
        }

        return docWellDetected;
    }


    private static int getFilesCount(File file) {
        File[] files = file.listFiles();
        int count = 0;
        for (File f : files)
            if (f.isDirectory())
                count += getFilesCount(f);
            else if(!Objects.equals(file.getName(), ".DS_Store"))
                count++;

        return count;
    }

}
