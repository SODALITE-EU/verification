pipeline {
  options { disableConcurrentBuilds() }
  agent { label 'docker-slave' }
  stages {
    stage ('Pull repo code from github') {
      steps {
        checkout scm
      }
    }
    stage ('Build semantic-reasoner') {
      when { 
          not { 
                triggeredBy 'UpstreamCause' 
          }
      }
      steps {
        build 'semantic-reasoner/master'
      }
    }
    stage ('Build verification components') {
      steps {
        sh  """ #!/bin/bash
                mvn clean install
            """
        archiveArtifacts artifacts: '**/*.war, **/*.jar', onlyIfSuccessful: true
      }
    }
	stage('Build docker images') {
            steps {
                sh "cd syntax; docker build -t toscasynverifier  -f Dockerfile ."
                sh "cd workflow; docker build -t workflowverifier -f Dockerfile ."
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
