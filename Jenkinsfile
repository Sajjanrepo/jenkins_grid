pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the GitHub repository
                git url: 'https://github.com/Sajjanrepo/jenkins_grid.git', branch: 'master'
            }
        }

        stage('Set up Python') {
            steps {
                // Set up Python environment and dependencies
                sh '''
                        pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Run Python scripts or tests
                sh '''
                    pytest -s -v -n 4 --html=report.html --self-contained-html
                '''
            }
        }
         stage('Publish Report') {
            steps {
                publishHTML (target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: false,
                    keepAll: true,
                    reportDir: './reports/',
                    reportFiles: 'report.html',
                    reportName: 'Test Report'
                ])
            }
        }
    }
}
