pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                sh '''
                    sudo docker stop flask-container 2>/dev/null || true
                    sudo docker rm flask-container 2>/dev/null || true
                    sudo docker rmi flask-app:latest 2>/dev/null || true
                    
                    sudo docker build -t flask-app .
                '''
            }
        }

        stage('Run') {
            steps {
                sh '''
                    sudo docker run -d  -p 5000:5000 --name flask-container flask-app:latest
                '''
            }
        }
    }
}
