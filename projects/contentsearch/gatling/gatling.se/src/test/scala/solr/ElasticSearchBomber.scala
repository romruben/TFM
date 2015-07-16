package solr

/**
 * Created by ruben on 15/07/15.
 */

import io.gatling.core.Predef._
import io.gatling.http.Predef._


class ElasticSearchBomber extends Simulation {

  // Define the scenario below
  val scn = scenario("Search").repeat(10000){
    exec(
      http("Search")
        .get("http://localhost:9200/test/_search?q=file:motorola&fields=_id")
    )
  }

  setUp(scn.inject(atOnceUsers(100)))
}
