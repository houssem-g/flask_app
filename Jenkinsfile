pipeline {
  agent any
  stages {
    stage('SCM') {
      steps {
        echo 'hello world'
      }
    }


    stage('build docker') {

      steps {
        
        sh 'sudo docker build -t flask-app .'
      }
    }
    stage("run docker container"){
      steps {
        sh "sudo docker run -p 5000:5000 --name app -d app "
      }
        
    }

    stage('test') {
      agent {
        docker {
          image 'python:3.7.2'
        }

      }
      steps {
        sh 'pip install -r ./app/requirements.txt'
        sh 'python3 ./app/test.py'
      }
    }

  }
  environment {
    scm = 'jenkins'
  }
  post {
    always {
      cleanWs()
    }

  }
}

