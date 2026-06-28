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
                sh 'docker --version'
            }
        }

        stage('Complete') {
            steps {
                echo 'Enterprise Monitor Pipeline Completed'
            }
        }
    }
}
