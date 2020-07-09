pipeline {
  agent any
  stages {
    stage('SCM') {
      steps {
        echo 'hello world'
      }
    }

    stage('build') {
      agent {
        docker {
          image 'python:3.7.2'
          args '-v /root/.m2/repository:/root/.m2/repository'
        }

      }
      steps {
        sh 'mvn clean compile'
      }
      steps {
        sh 'python test.py'
      }
    }

  }
  environment {
    scm = 'master'
  }
}