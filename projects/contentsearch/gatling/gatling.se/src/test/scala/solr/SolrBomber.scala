package solr

/**
 * Created by ruben on 15/07/15.
 */

import io.gatling.core.Predef._
import io.gatling.http.Predef._


class SolrBomber extends Simulation {

  // Define the scenario below
  val scn = scenario("Search").repeat(10000){
    exec(
      http("Search")
        .get("http://localhost:8983/solr/tfm/query?q=motorola&fl=id")
    )
  }

  setUp(scn.inject(atOnceUsers(100)))
}
