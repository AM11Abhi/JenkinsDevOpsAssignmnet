pipeline {
    agent any

    stages {

        stage('Build') {
            when {
                branch 'main'
            }
            steps {
                echo 'Building application (Main branch)'
            }
        }

        stage('Test') {
            when {
                anyOf {
                    branch 'main'
                    branch 'feature/*'
                    branch 'release/*'
                }
            }
            steps {
                echo 'Running tests'
            }
        }

        stage('Security Scan') {
            when {
                branch 'release/*'
            }
            steps {
                echo 'Running security scan'
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying application'
            }
        }
    }
}