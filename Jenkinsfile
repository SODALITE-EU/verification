pipeline {
  options { disableConcurrentBuilds() }
  agent { label 'docker-slave' }
  stages {
    stage ('Pull repo code from github') {
      steps {
        checkout scm
      }
    } 
    stage('Test syntax verification') {
        steps {
            sh  """ #!/bin/bash
			        cd syntax
                    python3 -m pip install -r requirements.txt                   
                    python3 -m pytest --pyargs -s ./tests --junitxml="results.xml" --cov=tosca --cov-report xml tests/
					cp *.xml $WORKSPACE
                """
            junit 'results.xml'
        }
    }	
    stage('test workflow verification') {
        steps {
            sh  """ #!/bin/bash
			        cd workflow
                    python3 -m pip install -r requirements.txt                    
                    python3 -m pytest --pyargs -s ./tests --junitxml="results.xml" --cov=pnmlpy --cov-report xml tests/
					cp *.xml $WORKSPACE
                """
            junit 'results.xml'
        }
    }
	stage('SonarQube analysis workflow'){
        environment {
          scannerHome = tool 'SonarQubeScanner'
        }
        steps {
            withSonarQubeEnv('SonarCloud') {
                sh  """ #!/bin/bash
                        cd "workflow"
                        ${scannerHome}/bin/sonar-scanner
                    """
            }
        }
    }
	stage('SonarQube analysis syntax'){
        environment {
          scannerHome = tool 'SonarQubeScanner'
        }
        steps {
            withSonarQubeEnv('SonarCloud') {
                sh  """ #!/bin/bash
                        cd "syntax"
                        ${scannerHome}/bin/sonar-scanner
                    """
            }
        }
    }
	stage('SonarQube analysis api'){
        environment {
          scannerHome = tool 'SonarQubeScanner'
        }
        steps {
            withSonarQubeEnv('SonarCloud') {
                sh  """ #!/bin/bash
                        cd "iacverifier"
                        ${scannerHome}/bin/sonar-scanner
                    """
            }
        }
    }
	stage('Build docker images') {
            steps {
                sh "cd syntax; docker build -t toscasynverifier  -f Dockerfile ."
                sh "cd workflow; docker build -t workflowverifier -f Dockerfile ."
				sh "cd iacverifier; docker build -t iacverifierapi -f Dockerfile ."
            }
    }
   
    stage('Push Dockerfile to DockerHub') {
            when {
               branch "master"
            }
            steps {
                withDockerRegistry(credentialsId: 'jenkins-sodalite.docker_token', url: '') {
                    sh  """#!/bin/bash                       
                            docker tag toscasynverifier sodaliteh2020/toscasynverifier:${BUILD_NUMBER}
                            docker tag toscasynverifier sodaliteh2020/toscasynverifier
                            docker push sodaliteh2020/toscasynverifier:${BUILD_NUMBER}
                            docker push sodaliteh2020/toscasynverifier
                            docker tag workflowverifier sodaliteh2020/workflowverifier:${BUILD_NUMBER}
                            docker tag workflowverifier sodaliteh2020/workflowverifier
                            docker push sodaliteh2020/workflowverifier:${BUILD_NUMBER}
                            docker push sodaliteh2020/workflowverifier
							docker tag iacverifierapi sodaliteh2020/iacverifierapi:${BUILD_NUMBER}
                            docker tag iacverifierapi sodaliteh2020/iacverifierapi
                            docker push sodaliteh2020/iacverifierapi:${BUILD_NUMBER}
                            docker push sodaliteh2020/iacverifierapi
                        """
                }
            }
    }
  }
  post {
    failure {
        slackSend (color: '#FF0000', message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
    }
    fixed {
        slackSend (color: '#6d3be3', message: "FIXED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})") 
    }
  }
}
