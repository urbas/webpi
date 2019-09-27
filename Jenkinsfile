pipeline {
  agent { label "raspbian" }

  stages {
    stage("Deploy") {
      when { tag "v*" }
      steps {
        withCredentials([string(credentialsId: 'urbas-dockerhub', variable: 'DOCKER_PASSWORD')]) {
          sh """
            cd backend
            sudo docker build -t urbas/webpi-backend-arm:$TAG_NAME --build-arg PYTHON_VERSION=\$(cat ../.python-version) .
            echo "$DOCKER_PASSWORD" | sudo docker login -u urbas --password-stdin
            sudo docker push urbas/webpi-backend-arm:$TAG_NAME
          """
        }
      }
    }
  }
}