#!groovy​
pipeline {
    agent any
    triggers {
        pollSCM ''
    }
    stages {

        stage("Run (Unit test)") {
            steps {
                sh 'make run-unit-test'
            }
        }

        stage("Deploy (Functions)") {
            steps {
                sh 'make deploy'
            }
        }

        stage("Run (Integrations)") {
            steps {
                sh 'make run-integration-test'
            }
        } 
    }
    post {
        always {
            script {
                // Notifier to be included later on
            }
        }
    }
}
