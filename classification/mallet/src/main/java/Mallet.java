/* Copyright (C) 2002 Univ. of Massachusetts Amherst, Computer Science Dept.
   This file is part of "MALLET" (MAchine Learning for LanguagE Toolkit).
   http://www.cs.umass.edu/~mccallum/mallet
   This software is provided under the terms of the Common Public License,
   version 1.0, as published by http://www.opensource.org.  For further
   information, see the file `LICENSE' included with this distribution. */


/**
 Takes a list of directory names as arguments, (each directory
 should contain all the text files for each class), performs a random train/test split,
 trains a classifier, and outputs accuracy on the testing and training sets.

 @author Andrew McCallum <a href="mailto:mccallum@cs.umass.edu">mccallum@cs.umass.edu</a>
 @edited by Rubén romero <a href="mailto:ruben.romcor@gmail.com">ruben.romcor@gmail.com</a>
 */


import cc.mallet.classify.*;
import cc.mallet.pipe.*;
import cc.mallet.pipe.iterator.FileIterator;
import cc.mallet.types.InstanceList;

import java.io.File;
import java.time.Duration;
import java.time.Instant;

public class Mallet {

    public static void main(String[] args) {

        String root = "/Users/ruben/Downloads/Formularios_clasificados/";

        File[] directories = {new File(root + "Contratos"),
                new File(root + "Desconocido"),
                new File(root + "Facturas"),
                new File(root + "Info"),
                new File(root + "Solicitud")};

        // Create the pipeline that will take as input {data = File, target = String for classname}
        // and turn them into {data = FeatureVector, target = Label}
        Pipe instancePipe = new SerialPipes(new Pipe[]{
                new Target2Label(),                              // Target String -> class label
                new Input2CharSequence(),                  // Data File -> String containing contents
                new CharSubsequence(CharSubsequence.SKIP_HEADER), // Remove UseNet or email header
                new CharSequence2TokenSequence(),  // Data String -> TokenSequence
                new TokenSequenceLowercase(),          // TokenSequence words lowercased
                new TokenSequenceRemoveStopwords(),// Remove stopwords from sequence
                new TokenSequence2FeatureSequence(),// Replace each Token with a feature index
                new FeatureSequence2FeatureVector(),// Collapse word order into a "feature vector"
                new PrintInputAndTarget(),
        });

        // Create an empty list of the training instances
        InstanceList ilist = new InstanceList(instancePipe);

        // Add all the files in the directories to the list of instances.
        // The Instance that goes into the beginning of the instancePipe
        // will have a File in the "data" slot, and a string from args[] in the "target" slot.
        ilist.addThruPipe(new FileIterator(directories, FileIterator.STARTING_DIRECTORIES));

        // Make a test/train split; ilists[0] will be for training; ilists[1] will be for testing
        InstanceList[] ilists = ilist.split(new double[]{.7, .3});

        //Testing NativeBayesTrainer
        ClassifierTrainer naiveBayesTrainer = nativeBayesTrainer(ilists);

        //Testing adaBoostTrainer
        adaBoostTrainer(ilists, naiveBayesTrainer);

        //Testing balancedWinnowTrainer
        balancedWinnowTrainer(ilists);

        //Testing decisionTreeTrainer
        decisionTreeTrainer(ilists);

        //Testing maxEntL1Trainer
        maxEntL1Trainer(ilists);

        //Testing c45Trainer
        c45Trainer(ilists);

        //Testing rankMaxEntTrainer
        rankMaxEntTrainer(ilists);

        //Testing mcMaxEntTrainer
        mcMaxEntTrainer(ilists);
    }

    private static void mcMaxEntTrainer(InstanceList[] ilists) {
        Instant before = Instant.now();
        ClassifierTrainer mcMaxEntTrainer = new MCMaxEntTrainer();
        Classifier classifier = mcMaxEntTrainer.train(ilists[0]);
        printResults(ilists, before, classifier);
    }

    private static void rankMaxEntTrainer(InstanceList[] ilists) {
        Instant before = Instant.now();
        ClassifierTrainer rankMaxEntTrainer = new RankMaxEntTrainer();
        Classifier classifier = rankMaxEntTrainer.train(ilists[0]);
        printResults(ilists, before, classifier);
    }

    private static void c45Trainer(InstanceList[] ilists) {
        Instant before = Instant.now();
        ClassifierTrainer c45Trainer = new C45Trainer();
        Classifier classifier = c45Trainer.train(ilists[0]);
        printResults(ilists, before, classifier);
    }

    private static void maxEntL1Trainer(InstanceList[] ilists) {
        Instant before = Instant.now();
        ClassifierTrainer maxEntL1Trainer = new MaxEntL1Trainer();
        Classifier classifier5 = maxEntL1Trainer.train(ilists[0]);
        printResults(ilists, before, classifier5);
    }

    private static void decisionTreeTrainer(InstanceList[] ilists) {
        Instant before = Instant.now();
        ClassifierTrainer decisionTreeTrainer = new DecisionTreeTrainer();
        Classifier classifier = decisionTreeTrainer.train(ilists[0]);
        printResults(ilists, before, classifier);
    }

    private static void balancedWinnowTrainer(InstanceList[] ilists) {
        Instant before = Instant.now();
        ClassifierTrainer balancedWinnowTrainer = new BalancedWinnowTrainer();
        Classifier classifier = balancedWinnowTrainer.train(ilists[0]);
        printResults(ilists, before, classifier);
    }

    private static void adaBoostTrainer(InstanceList[] ilists, ClassifierTrainer naiveBayesTrainer) {
        Instant before = Instant.now();
        ClassifierTrainer adaBoostTrainer = new AdaBoostTrainer(naiveBayesTrainer);
        Classifier classifier = adaBoostTrainer.train(ilists[0]);
        printResults(ilists, before, classifier);
    }

    private static ClassifierTrainer nativeBayesTrainer(InstanceList[] ilists) {
        Instant before = Instant.now();
        ClassifierTrainer naiveBayesTrainer = new NaiveBayesTrainer();
        Classifier classifier = naiveBayesTrainer.train(ilists[0]);
        printResults(ilists, before, classifier);
        return naiveBayesTrainer;
    }

    private static void printResults(InstanceList[] ilists, Instant before, Classifier classifier) {
        System.out.println("The training accuracy is " + classifier.getAccuracy(ilists[0]));
        System.out.println("The testing accuracy is " + classifier.getAccuracy(ilists[1]));
        System.out.println("Time is " + Duration.between(before, Instant.now()));
    }

}