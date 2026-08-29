pipeline {

    agent {
        label 'my-slave'
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/ManishMessi1010/microservices-project.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker build -t manishh08/auth-service ./auth-service'
                sh 'docker build -t manishh08/products-service ./products-service'
                sh 'docker build -t manishh08/orders-service ./orders-service'
            }
        }

        stage('Remove Old Containers') {
            steps {
                sh 'docker rm -f auth-container || true'
                sh 'docker rm -f products-container || true'
                sh 'docker rm -f orders-container || true'
            }
        }

        stage('Push Images to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'manish-dockerhub',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'

                    sh 'docker push manishh08/auth-service'
                    sh 'docker push manishh08/products-service'
                    sh 'docker push manishh08/orders-service'

                    sh 'docker logout'
                }
            }
        }
