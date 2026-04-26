pipeline {
    agent any

    environment {
        APP_NAME = "aceest-app"
        DOCKER_IMAGE = "aceest-app:jenkins"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv || true
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest -q
                '''
            }
        }

//         stage('SonarQube Analysis') {
//             steps {
//                 script {
//                     def scannerHome = tool 'sonar-scanner'
//                     withSonarQubeEnv('SonarQube') {
//                         withCredentials([string(credentialsId: 'SONAR_TOKEN', variable: 'SONAR_TOKEN')]) {
//                             sh """
//                             . venv/bin/activate
//                             ${scannerHome}/bin/sonar-scanner \
//                               -Dsonar.projectKey=aceest-app \
//                               -Dsonar.sources=. \
//                               -Dsonar.host.url=http://host.docker.internal:9000 \
//                               -Dsonar.login=$SONAR_AUTH_TOKEN
//                             """
//                         }
//                     }
//                 }
//             }
//         }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml
                '''
            }
        }
    }
}