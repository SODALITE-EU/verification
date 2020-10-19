# verification

This module verifies the TOSCA and IaC artifacts for their inconsistencies and constraints. 

## Note
Most of the verification of TOSCA and ansible properties are done by the project “semantic-reasoner”.

The information about building semantic reasoner can be found at
 ` https://github.com/SODALITE-EU/semantic-reasoner `

## Deployment

The built artifact is a web application (.war file) that can be deployed in any Web server. 

## Docker Image Building and Usage : TOSCA Syntax Verifier
```
sudo docker build -t sodalite/toscasynverifier .
sudo docker run -p 5000:5000 -d --name=toscasynverifier sodalite/toscasynverifier
sudo docker start toscasynverifier
sudo docker logs toscasynverifier
sudo docker stop toscasynverifier
sudo docker rm  toscasynverifier
sudo docker rmi sodalite/toscasynverifier
```
## Docker Image Building and Usage : PetriNet Verifier
```
sudo docker build -t sodalite/workflowverifier .
sudo docker run -p 5000:5000 -d --name=workflowverifier sodalite/workflowverifier
sudo docker start workflowverifier
sudo docker logs workflowverifier
sudo docker stop workflowverifier
sudo docker rm  workflowverifier
sudo docker rmi sodalite/workflowverifier
```
## Run Docker Compose
```
sudo docker-compose up
sudo docker image ls
```
## REST APIs
# TOSCA
```
http://{serverIP}:5000/errors/tosca/file
```
Send the TOSCA file as multipart/form-data (name:” file”, value: actual file)

# Petri Net based Workflow
```
http://{serverIP}:5000/errors/workflow/file
```
Send the PNML (Petri Net Markup Language) file as multipart/form-data (name:” file”, value: actual file)
