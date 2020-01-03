package nl.jads.tosca.restapi;

import nl.jads.tosca.ToscaVerifierKBApi;
import nl.jads.tosca.dto.VerificationRecord;
import nl.jads.tosca.dto.VerificationReport;
import nl.jads.tosca.dto.VerifierInput;

import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

@Path("/verifier")
//@Api()
public class BugPredictorService {

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    @Consumes(MediaType.APPLICATION_JSON)
//    @ApiOperation(
//            value = "Returns the verification in the IaC codes",
////			response = String.class,
//            responseContainer = "List")
    public Response verify(VerifierInput verifierInput) throws IOException {
        ToscaVerifierKBApi kbApi = new ToscaVerifierKBApi();
        VerificationReport bugReport = findErrors(kbApi, verifierInput);
        kbApi.shutDown();
        return Response.ok(bugReport).build();
    }

    private VerificationReport findErrors(ToscaVerifierKBApi kbApi, VerifierInput bugInput) throws IOException {
        VerificationReport bugReport = new VerificationReport();
        List<VerificationRecord> bugs = new ArrayList<>();
        bugReport.setActionId(bugInput.getActionId());
        bugReport.setDeploymentId(bugInput.getDeploymentId());
        bugReport.setBugs(bugs);
        return bugReport;
    }

}
