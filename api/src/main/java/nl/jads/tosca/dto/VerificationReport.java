package nl.jads.tosca.dto;

import com.fasterxml.jackson.databind.PropertyNamingStrategy;
import com.fasterxml.jackson.databind.annotation.JsonNaming;

import java.util.List;

@JsonNaming(PropertyNamingStrategy.SnakeCaseStrategy.class)
public class VerificationReport {
    private String actionId;
    private String deploymentId;
    private List<VerificationRecord> bugs;

    public String getActionId() {
        return actionId;
    }

    public void setActionId(String actionId) {
        this.actionId = actionId;
    }

    public String getDeploymentId() {
        return deploymentId;
    }

    public void setDeploymentId(String deploymentId) {
        this.deploymentId = deploymentId;
    }

    public List<VerificationRecord> getBugs() {
        return bugs;
    }

    public void setBugs(List<VerificationRecord> bugs) {
        this.bugs = bugs;
    }
}
