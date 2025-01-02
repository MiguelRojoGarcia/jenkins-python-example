pipeline{
    agent any
    environment{
        ADMINISTRATOR_EMAIL="mrojo@iar-soft.com"
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
        failure {
            emailext(
                subject: "ERROR: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' ha fallado",
                body: """<p>Hola,</p>
                         <p>El job de Jenkins <b>${env.JOB_NAME}</b> con número de build <b>${env.BUILD_NUMBER}</b> ha fallado.</p>
                         <p>Detalles del error:</p>
                         <pre>${currentBuild.currentResult}</pre>
                         <p>Puedes revisar el log completo en el siguiente enlace: 
                         <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>""",
                to: "${ADMINISTRATOR_EMAIL}",
                mimeType: 'text/html'
            )
        } 
        always { 
            cleanWs()            
        }
    }
}