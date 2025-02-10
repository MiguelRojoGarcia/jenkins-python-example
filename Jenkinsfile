pipeline{
    agent{
        docker { image 'python:3.12-slim'}
    }
    stages{
        stage('Install depedencies'){
            sh 'pip install --no-cache-dir -r requirements.txt || true'
        }
        stage('Run tests'){
            sh 'pytest tests.py'
        }
    }
}