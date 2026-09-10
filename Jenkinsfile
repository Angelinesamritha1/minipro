pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Run') {
            steps {
                sh 'docker rm -f flask-container || true'
                sh 'docker run -d --name flask-container -p 5000:5000 flask-app'
            }
        }
    }
}
