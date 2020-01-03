package nl.jads.tosca;

import kb.KBApi;

import java.io.IOException;

public class AnsibleVerifierKBApi extends KBApi {

    String PREFIXES = "PREFIX tosca: <https://www.sodalite.eu/ontologies/tosca/> \r\n" +
            "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\n" +
            "PREFIX soda: <https://www.sodalite.eu/ontologies/sodalite-metamodel/> \r\n" +
            "PREFIX DUL: <http://www.loa-cnr.it/ontologies/DUL.owl#> \r\n" +
            "PREFIX dcterms: <http://purl.org/dc/terms/> \r\n" +
            "PREFIX owl: <http://www.w3.org/2002/07/owl#> \r\n";

    public static String DCTERMS = "http://purl.org/dc/terms/";
    public static String DUL = "http://www.loa-cnr.it/ontologies/DUL.owl#";
    public static String TOSCA = "https://www.sodalite.eu/ontologies/tosca/";
    public static String SODA = "https://www.sodalite.eu/ontologies/sodalite-metamodel/";

    public AnsibleVerifierKBApi() {
        super();
    }

    public void shutDown() {
        super.shutDown();
    }

    public boolean validate(){
        //TODO
        return false;
    }
    public static void main(String[] args) throws IOException {
        AnsibleVerifierKBApi kbApi = new AnsibleVerifierKBApi();
    }
}
