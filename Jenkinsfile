pipeline {
    agent any
    environment {
        DOCKER_HUB_REPO = '5unnysunny/scalculator'  // Replace with your Docker Hub repo
        DOCKER_CREDENTIALS_ID = 'docker-hub-credentials'  // Matches your Jenkins credential ID
        PATH = "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    }
    stages {
        stage('Pull Repo') {
            steps {
                git url: 'https://github.com/anirudh-pathaneni/ScientificCalculator-DevOps', branch: 'main'  // Replace with your repo
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest test_scalculator.py'  // Assumes your test file
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
                sh 'ansible-playbook -i localhost, ansible/deploy.yml --extra-vars "image_tag=${BUILD_NUMBER}"'  // Assumes your Ansible playbook
            }
        }
        // Optional Email Stage
        stage('Send Email') {
            steps {
                emailext subject: "Pipeline ${currentBuild.currentResult}", body: "Build ${env.BUILD_NUMBER} ${currentBuild.currentResult}", to: 'pathaneni.anirudh@iiitb.ac.in'
            }
        }
    }
    post {
        always {
            cleanWs()  // Clean up workspace
        }
    }
}