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

    stage('Test code') {
      agent {
        dockerfile {
          filename 'Dockerfile.db'
        }

      }
      steps {
        echo 'DB Connexion setup'
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