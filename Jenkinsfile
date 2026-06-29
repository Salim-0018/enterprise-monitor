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

        stage('Verify Image') {
            steps {
                sh 'docker images'
            }
        }

        stage('Complete') {
            steps {
                echo 'Enterprise Monitor Pipeline Completed Successfully!'
            }
        }
    }
}
