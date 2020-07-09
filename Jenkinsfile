pipeline {
  agent any
  stages {
    stage('SCM') {
      steps {
        echo 'hello world'
      }
    }

    stage('build') {
      parallel {
        stage('build') {
          agent {
            docker {
              args '-v /root/.m2/repository:/root/.m2/repository'
              image 'python:3.7.2'
            }

          }
          steps {
            sh 'mvn clean compile'
          }
        }

        stage('test') {
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