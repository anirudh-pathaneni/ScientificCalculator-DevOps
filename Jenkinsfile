pipeline {
    agent any
    environment {
        DOCKER_HUB_REPO = '5unnysunny/scalculator'
        DOCKER_CREDENTIALS_ID = 'docker-hub-credentials'
    }
    stages {
        stage('Pull Repo') {
            steps {
                git url: 'https://github.com/anirudh-pathaneni/ScientificCalculator-DevOps', branch: 'main'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest test_scalculator.py' 
            }
        }
        stage('Build Image') {
            steps {
                script {
                    dockerImage = docker.build("${DOCKER_HUB_REPO}:${env.BUILD_NUMBER}")
                }
            }
        }
        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS_ID}", usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh "echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} --password-stdin"
                }
            }
        }
        stage('Push Image') {
            steps {
                sh "docker push ${DOCKER_HUB_REPO}:${env.BUILD_NUMBER}"
            }
        }
        stage('Deploy') {
            steps {
                sh 'ansible-playbook -i localhost, ansible/deploy.yml --extra-vars "image_tag=${BUILD_NUMBER}"'  
            }
        }
        stage('Send Email') {
            steps {
                emailext subject: "Pipeline ${currentBuild.currentResult}", body: "Build ${env.BUILD_NUMBER} ${currentBuild.currentResult}", to: 'pathaneni.anirudh9@gmail.com'
            }
        }
    }
    post {
        always {
            cleanWs()  // Clean up workspace
        }
    }
}