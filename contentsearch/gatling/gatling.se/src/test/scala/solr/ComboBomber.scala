package solr

/**
 * Created by ruben on 15/07/15.
 */

import io.gatling.core.Predef._
import io.gatling.http.Predef._


class ComboBomber extends Simulation {

  // Define the scenario below
  val scn = scenario("Search").repeat(10000){
    exec(
      http("Search")
        .get("http://localhost:9200/5septiembre/_search?q=file:%22remittance%20to%20another%20bank%22+%22stands%20for%20insurance%20payment%22&fields=_id")
    )
  }

  setUp(scn.inject(atOnceUsers(100)))
}
