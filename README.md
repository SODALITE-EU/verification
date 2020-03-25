# verification

This module verifies the TOSCA and IaC artifacts for their inconsistencies and constraints. 

## Prerequisites
This module depends on the SODALITE sub-project “semantic-reasoner”. Thus, first built it

The information about building semantic reasoner can be found at
 ` https://github.com/SODALITE-EU/semantic-reasoner `

## Build Process 

Use mvn to build this module project.

```
mvn clean install 

```
This requires maven 3.x 

## Deployment

The built artifact is a web application (.war file) that can be deployed in any Web server. 
