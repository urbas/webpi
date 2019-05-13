pipeline {
  agent { label "raspbian && webpi" }

  stages {
    stage("Build") {
      steps {
        sh "git clean -ffdx ."
        sh """
          cd backend
          sudo docker build -t webpi-backend:$GIT_COMMIT --build-arg PYTHON_VERSION=\$(cat ../.python-version) .
        """
        sh """
          cd frontend
          mkdir deployment
          sudo docker build -t webpi-frontend:$GIT_COMMIT --build-arg NODE_VERSION=\$(cat ../.nvmrc) .
          sudo docker run -i webpi-frontend:$GIT_COMMIT | tar -xvf - -C deployment
        """
      }
    }

    stage("Deploy") {
      steps {
        sh "sudo docker kill webpi-backend || echo 'The container was not running...'"
        sh "sudo docker rm webpi-backend || echo 'The container did not exist...'"
        sh "sudo docker run -d -p 5000:5000 --name webpi-backend webpi-backend:$GIT_COMMIT"
        sh "rsync -Pav frontend/deployment/ /var/lib/webpi_frontend/"
      }
    }
  }
}