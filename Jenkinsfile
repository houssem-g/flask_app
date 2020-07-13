pipeline {
  agent any
  stages {
    stage('SCM') {
      steps {
        echo 'hello world'
      }
    }

    stage('run') {
      parallel {
        stage('build') {
          agent {
            docker {
              image 'python:3.7.2'
            }

          }
          steps {
            sh 'pip install -r requirements.txt'
            sh 'python3 ./src/main/ressource/app.py'
          }
        }

        stage('test') {
          agent {
            docker {
              image 'python:3.7.2'
            }

          }
          steps {
            sh './job.sh'
          }
        }

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