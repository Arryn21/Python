pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository from the default branch (master/main)
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                // Install dependencies
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate.bat
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest and generate an HTML report
                bat '''
                call venv\\Scripts\\activate.bat
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
