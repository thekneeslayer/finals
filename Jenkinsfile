pipeline {
    agent any

    environment {
        VENV_DIR = ".venv"
        PYTHON = "python"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                bat '''
                %PYTHON% -m venv %VENV_DIR%
                call %VENV_DIR%\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call %VENV_DIR%\\Scripts\\activate
                pytest
                '''
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                echo Deploying Flask Application...

                REM Restart Flask service if running via NSSM
                nssm restart FlaskApp || echo "Service not found, skipping restart"

                echo Deployment completed
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Build, Test, and Deployment succeeded'
        }
        failure {
            echo '❌ Build or Tests failed – Deployment skipped'
        }
    }
}
