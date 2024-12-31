pipeline{
    agent any
    environment{
        VERSION="1.5"
        DATE="""${
            sh(
                returnStdout:true,
                script: 'echo $(date +%F)'
            )
        }"""
        MACHINE = """${
            sh(
                returnStdout:true,
                script: 'uname -n'
            )
        }"""
    }
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
        stage('Test variables'){
            steps{
                echo "${VERSION}" 
                echo "${DATE}" 
                echo "${MACHINE}" 
            }
        }
    }
    post { 
        always { 
            cleanWs()
        }
    }
}