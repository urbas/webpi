pipeline {
  agent { label "raspbian" }

  stages {
    stage("Build") {
      steps {
        sh "env"
      }
    }

    stage("Deploy") {
      when { tag "v*" }
      steps {
        sh "git clean -ffdx ."
        withCredentials([string(credentialsId: 'urbas-dockerhub', variable: 'DOCKER_PASSWORD')]) {
          sh """
            cd backend
            env
            VERSION=\$(git describe --tags '--match=v*')
            sudo docker build -t urbas/webpi-backend-arm:\$VERSION --build-arg PYTHON_VERSION=\$(cat ../.python-version) .
            echo "$DOCKER_PASSWORD" | sudo docker login -u urbas --password-stdin
            sudo docker push urbas/webpi-backend-arm:\$VERSION
          """
        }
      }
    }
  }
}