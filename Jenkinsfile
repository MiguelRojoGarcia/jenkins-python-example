pipeline{
    agent any

    stages {
        stage('Install dependencies'){
            steps{
                sh 'pip install -r requirements.txt --break-system-packages'
            }
        }
        stage('Run tests'){
             steps{
                sh 'pytest tests.py'
            }
        }
        stage('Run application'){
            steps{
                sh 'python3 main.py'
            }
        }
         stage('Creating tag'){
            steps{
                sh "git tag ${env.BUILD_NUMBER}.0"
                sh "git push origin --tags"
            }
        }
    }
    post { 
        always { 
            cleanWs()
        }
    }
}