pipeline {
    agent any

    environment {
        IMAGE_NAME = 'weather-app'
        IMAGE_TAG = 'latest'
        REGISTRY_URL = 'lakshmisatya'  // Replace with your DockerHub username
        K8S_NAMESPACE = 'default'  // Modify according to your Kubernetes namespace
    }

    stages {
        stage('Git Checkout') {
            steps {
                git 'https://github.com/SatyaSri-154/Weather-App-with-Python-Django.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG .'
                }
            }
        }

        stage('Login to DockerHub') {
            steps {
                script {
                    sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    sh 'docker push $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh 'kubectl apply -f k8s/deployment.yaml'
                    sh 'kubectl apply -f k8s/service.yaml'
                }
            }
        }
    }
}
