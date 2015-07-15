# Gatling

## Install Scala

## Maven Archetype

### Prerequisites

    * An IDE for Scala
    * Maven

### Creating a project using the Archetype

```
mvn archetype:generate
```

When prompted, type "gatling":

```
Choose a number or apply filter (format: [groupId:]artifactId, case sensitive contains):
```

You should then see:

```
Choose archetype:
1: remote -> io.gatling.highcharts:gatling-highcharts-maven-archetype (gatling-highcharts-maven-archetype)
```

And type 1 and select the groupId and artifactId.


## Using the Archetype

The project structure should look like that:

![http://gatling.io/docs/2.0.3/_images/archetype_structure.png](http://gatling.io/docs/2.0.3/_images/archetype_structure.png)



The archetype structure closely follows the bundle’s structure :

* **data** is where the files for your feeders are to be stored
* **request-bodies** is where your request bodies are to be stored
* **Your simulations** will live under src/test/scala

## Running Gatling

Simply launch the Engine class in your IDE. Simulation reports will be written in the target directory.


## Acknowledgements

* http://gatling.io/docs/2.0.3/extensions/maven_archetype.html
* http://www.alexecollins.com/gatling-in-10-minutes/

## Execution

to run the simulations it must be executed the "Engine" file in your IDE.

## Reports

The test reports are in target/results/ folder.