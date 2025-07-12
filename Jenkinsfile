pipeline {
    agent any

    environment {
        IMAGE_NAME = 'lawest98/djangoapp'
    }

    stages {
        stage('Clone') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}:${env.BUILD_NUMBER}")
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        sh """
                          echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                          docker push ${IMAGE_NAME}:${env.BUILD_NUMBER}
                          docker tag ${IMAGE_NAME}:${env.BUILD_NUMBER} ${IMAGE_NAME}:latest
                          docker push ${IMAGE_NAME}:latest
                        """
                    }
                }
            }
        }
    }

    post {
        success {
            echo "✅ Image pushed: ${IMAGE_NAME}:${env.BUILD_NUMBER}"
        }
        failure {
            echo '❌ Build or push failed!'
        }
    }
}
