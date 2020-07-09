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
              args '-v /root/.m2/repository:/root/.m2/repository'
              image 'maven:3-alpine'
            }

          }
          steps {
            sh 'mvn clean compile'
          }
        }

        stage('test') {
          agent {
            docker {
              image 'python:3.7.2'
            }

          }
          steps {
            sh 'python test.py'
          }
        }

      }
    }

  }
  environment {
    scm = 'master'
  }
}