pipeline {
    agent any
    environment {
        // Must match the image name you intend to push
        DOCKER_IMAGE_REPO = "shehrozkhan624/static-site-app"
        DOCKER_IMAGE_TAG = "${DOCKER_IMAGE_REPO}:${env.BUILD_NUMBER}"
        // Must match the name of your Kubernetes Deployment YAML
        K8S_DEPLOYMENT = "deployment"
    }
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/BSSE23102/jenkins-ci-dd'
            }
        }
        
        stage('Build Image') { 
            steps {
                // Ensure this path is correct relative to the Jenkins workspace root
                sh "docker build -t ${DOCKER_IMAGE_TAG} ./app/frontend"
            }
        }
        
        stage('Push Image') { 
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USER')]) {
                    sh "docker login -u ${DOCKER_USER} -p ${DOCKER_PASSWORD}"
                    sh "docker push ${DOCKER_IMAGE_TAG}"
                }
            }
        }
        
        stage('Deploy to K8s') { 
            steps {
                // Task: Deploy to K8s
                // Updates the Deployment named 'frontend-deployment' to use the new image tag
                sh "kubectl set image deployment/${K8S_DEPLOYMENT} static-nginx-container=${DOCKER_IMAGE_TAG}"
                
                // Task: Confirm pod updated
                sh "kubectl rollout status deployment/${K8S_DEPLOYMENT}"
            }
        }
    }
}