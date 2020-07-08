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
          image 'maven:3-alpine'
          args '-v /root/.m2/repository:/root/.m2/repository'
        }

      }
      steps {
        sh 'mvn clean compile'
      }
    }

  }
  environment {
    scm = 'master'
  }
}