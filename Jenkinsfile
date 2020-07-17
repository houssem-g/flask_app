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
        sh 'docker build -t flask-app .'
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

    stage('') {
      steps {
        sh 'pip install -r ./app/requirements.txt'
        sh 'pylint ./app/app.py'
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