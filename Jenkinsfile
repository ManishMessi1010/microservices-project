pipeline {

    agent {
        label 'my-slave'
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/ManishMessi1010/microservices-project.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker build -t manishh08/auth-service ./auth-service'
                sh 'docker build -t manishh08/product-service ./product-service'
                sh 'docker build -t manishh08/order-service ./order-service'
            }
        }

        stage('Cleanup') {
            steps {
                sh 'docker rm -f auth-container || true'
                sh 'docker rm -f product-container || true'
                sh 'docker rm -f order-container || true'
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
                    sh 'docker push manishh08/product-service'
                    sh 'docker push manishh08/order-service'

                    sh 'docker logout'
                }
            }
        }
    }
}
