pipeline{
    agent any
    options {
        //Time between builds
        rateLimitBuilds(throttle:([count: 5, durationName: 'minute', userBoost: false]))        
        // Max build log
        buildDiscarder logRotator(
                artifactDaysToKeepStr: '',
                artifactNumToKeepStr: '',
                daysToKeepStr: '1',
                numToKeepStr: '1'
            )
    }
    /*
    triggers{
        // Basic: pull every minute
        //pollSCM '* * * * *'
        // Improvement: Github hook
        //githubPush()
    }
    */
    environment{
        ADMINISTRATOR_EMAIL="mrojo@iar-soft.com"
        ENV="DEV"
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
                writeFile(file: "${DATE}.log", text:"[${env.JOB_NAME}][${env.BUILD_NUMBER}] - Install requirements...")
                sh 'pip install -r requirements.txt --break-system-packages'
            }
        }
        stage('Run tests'){
             steps{
                writeFile(file: "${DATE}.log", text:"[${env.JOB_NAME}][${env.BUILD_NUMBER}] - Running tests...")
                sh 'pytest tests.py'
            }
        }
        stage('Run database backups'){
            when{
                environment name: "ENV", value: "PROD"
            }
            steps{
                writeFile(file: "${DATE}.log", text:"[${env.JOB_NAME}][${env.BUILD_NUMBER}] - Running database backups...")
                sh 'echo "Running backups..."'
            }
        }
        stage('Run application'){
            steps{
                writeFile(file: "${DATE}.log", text:"[${env.JOB_NAME}][${env.BUILD_NUMBER}] - Running application...")
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