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
    }
    post { 
        success {
             script {
                    def version = "v${env.BUILD_NUMBER}.0" 
                    def commitId = sh(script: "git rev-parse HEAD", returnStdout: true).trim()
                    echo "Creando y empujando el tag ${version} para el commit ${commitId}"

                    sh "git tag -a ${version} -m 'Creando tag ${version} en el commit ${commitId}'"
                    sh "git push origin ${version}"
                }
        }
        always { 
            cleanWs()
        }
    }
}