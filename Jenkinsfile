pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Repository Checked Out'
            }
        }

        stage('Build') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t enterprise-monitor:latest .'
            }
        }

      stage('Verify image') {
          steps {
               sh 'Docker image'
            }
       }


        stage('Complete') {
            steps {
                echo 'Enterprise Monitor Pipeline Completed'
            }
        }
    }
}
