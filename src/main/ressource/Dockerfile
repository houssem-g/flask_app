# base image
FROM jenkinsci/blueocean
USER root
# install dependencies
# RUN apk update \
#     && apk add --virtual build-deps gcc python3-dev musl-dev \
#     && apk add postgresql-dev \
#     && pip install psycopg2-binary \
#     && apk del build-deps

COPY . /ressource

WORKDIR /ressource

RUN pip install -r requirements.txt
RUN -v ./jenkins-data:/var/jenkins_home
RUN -v /var/run/docker.sock:/var/run/docker.sock

EXPOSE 8080


# pipeline {
#   agent any
#   stages {
#     stage('SCM') {
#       steps {
#         echo 'hello world'
#       }
#     }

#     stage('run') {
#       parallel {
#         stage('build') {
#           agent {
#             docker {
#               args '-v /root/.m2/repository:/root/.m2/repository'
#               image 'maven:3-alpine'
#             }

#           }
#           steps {
#             sh 'mvn clean compile'
#           }
#         }

#         stage('test') {
#           agent {
#             docker {
#               image 'python:3.7.2'
#             }

#           }
#           steps {
#             sh './job.sh'
#           }
#         }

#       }
#     }

#   }
#   environment {
#     scm = 'master'
#   }
#   post {
#     always {
#       cleanWs()
#     }

#   }
# }