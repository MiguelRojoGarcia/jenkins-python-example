node{
    stage('Install depedencies...'){
        sh 'pip install --no-cache-dir -r requirements.txt || true'
    }
    stage('Runing tests...'){
        sh 'pytest tests.py'
    }
    stage('Run application'){
        sh 'python3 main.py'
    }
}

