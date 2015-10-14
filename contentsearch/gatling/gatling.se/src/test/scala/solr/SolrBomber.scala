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
        .get("http://localhost:8983/solr/5septiembre_shard1_replica1/select?q=%22Operation%3Aremittance+to+another+bank%22++AND+%22stands+for+insurance+payment%22&rows=100&wt=json&indent=true")
    )

  }

  setUp(scn.inject(atOnceUsers(100)))
}
