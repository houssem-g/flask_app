pipeline {
  agent any
  stages {
    stage('SCM') {
      steps {
        echo 'hello world'
      }
    }

    stage('Build docker') {
      parallel {
        stage('build docker') {
          steps {
            sh 'docker build -t flask-app .'
          }
        }

        stage('Quality code') {
          agent {
            docker {
              image 'python:3.7.2'
            }

          }
          steps {
            sh 'pip install -r ./app/requirements.txt'
            sh 'pip install psycopg2==2.8.5'
            sh 'pylint ./app/app.py || exit 0'
          }
        }

      }
    }

    stage('Test Unitary') {
      steps {
        sh 'docker-compose up app'
      }
    }

  }
  environment {
    scm = 'master'
  }
  post {
    always {
      cleanWs()
    }

  }
}