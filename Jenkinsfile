pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clone the repository
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                // Install dependencies
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest and generate an HTML report
                sh '''
                source venv/bin/activate
                pytest --html=report.html
                '''
            }
        }
    }

    post {
        always {
            // Archive the test report
            archiveArtifacts artifacts: 'report.html', fingerprint: true
        }
        success {
            echo 'Build and tests were successful!'
        }
        failure {
            echo 'Build or tests failed!'
        }
    }
}
