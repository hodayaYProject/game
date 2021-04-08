pipeline {
  environment {
    dockerImage = ''
  }
  agent any
  options {buildDiscarder(logRotator(daysToKeepStr: '5', numToKeepStr: '20'))}
  stages {
    stage('Cloning Git') {
      steps {
        script {
            properties([pipelineTriggers([pollSCM('30 * * * *')])])
        }
        git 'https://github.com/hodayaYProject/game.git'
      }
    }
    stage('Building image') {
      steps{
        script {
             dockerImage = docker.build "WoG"
        }
      }
    }
     stage('run docker container'){
       steps{
         bat 'docker-compose up -d'
         bat 'python test/e2e.py'
         bat 'docker-compose down'
       }
    }
    stage('Remove Unused docker image') {
      steps{
        bat "docker rmi WoG:$BUILD_NUMBER"
      }
    }
  }
}