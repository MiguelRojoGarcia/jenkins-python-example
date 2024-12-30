pipeline{
    agent any

    stages {
        stage('Install dependencies'){
            steps{
                sh 'pip install -r /var/scripts/python/requirements.txt --break-system-packages'
            }
        }
        stage('Run tests'){
             steps{
                sh 'pytest /var/scripts/python/tests.py'
            }
        }
         stage('Run application'){
            steps{
                sh 'python3 /var/scripts/python/main.py'
            }
        }
    }
    post { 
        always { 
            cleanWs()
        }
    }
}