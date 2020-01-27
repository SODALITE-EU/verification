package nl.jads.tosca;

import kb.dto.Attribute;
import kb.dto.Property;
import kb.repository.KB;
import kb.utils.MyUtils;
import kb.utils.QueryUtil;
import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.Value;
import org.eclipse.rdf4j.query.BindingSet;
import org.eclipse.rdf4j.query.TupleQueryResult;

import java.io.IOException;
import java.util.HashSet;
import java.util.Set;

public class ToscaVerifierKBApi {

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
    private KB kb;

    public ToscaVerifierKBApi(KB kb) {
        this.kb = kb;
    }

    public void shutDown() {
        kb.shutDown();
    }

    public Set<Attribute> getAllAttributes() throws IOException {
        Set<Attribute> attributes = new HashSet<>();
        String sparql = MyUtils.fileToString("sparql/getAllAttributes.sparql");
        String query = PREFIXES + sparql;
        TupleQueryResult result = QueryUtil.evaluateSelectQuery(kb.getConnection(), query);

        while (result.hasNext()) {
            BindingSet bindingSet = result.next();
            IRI attr = (IRI) bindingSet.getBinding("attribute").getValue();
            IRI concept = (IRI) bindingSet.getBinding("p").getValue();

            Attribute a = new Attribute(attr);
            a.setClassifiedBy(concept);

            attributes.add(a);
        }
        result.close();
        return attributes;
    }

    public Set<Property> getProperties() throws IOException {
        Set<Property> properties = new HashSet<>();
        String sparql = MyUtils.fileToString("sparql/getAllProperties.sparql");
        String query = PREFIXES + sparql;
        TupleQueryResult result = QueryUtil.evaluateSelectQuery(kb.getConnection(), query);

        while (result.hasNext()) {
            BindingSet bindingSet = result.next();
            IRI p1 = (IRI) bindingSet.getBinding("property").getValue();
            IRI concept = (IRI) bindingSet.getBinding("concept").getValue();
            Value _value = bindingSet.hasBinding("value") ? bindingSet.getBinding("value").getValue() : null;

            Property a = new Property(p1);
            a.setClassifiedBy(concept);
            if (_value != null)
                a.setValue(_value, kb);

            properties.add(a);
        }
        result.close();
        return properties;
    }

    public boolean checkTypeCoherence() {
        //TODO
        return false;
    }

    public boolean checkCapabilityType() {
        //TODO
        return false;
    }

    public boolean checkCapabilitiesType() {
        //TODO
        return false;
    }

    public boolean checkRelationshipType() {
        //TODO
        return false;
    }

    public boolean checkRelationship() {
        //TODO
        return false;
    }

    public boolean checkValidSourceTypesNode() {
        //TODO
        return false;
    }

    public boolean checkValidSourceTypesCapability() {
        //TODO
        return false;
    }

    public boolean validate() {
        //TODO
        return false;
    }

    public static void main(String[] args) throws IOException {
        ToscaVerifierKBApi kbApi = new ToscaVerifierKBApi(new KB());
    }
}
