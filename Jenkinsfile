pipeline {
    agent any
    stages {
        stage('compile Stage') {
            steps {
                withMaven(maven : 'maven_3_8_4'){
                    sh 'mvn clean compile'
                }
            }
        }
        stage('Testing Stage') {
            steps {
                withMaven(maven : 'maven_3_8_4'){
                    sh 'mvn test'
                }
            }
        }
        stage('Deployement Stage') {
            steps {
                withMaven(maven : 'maven_3_8_4'){
                    sh 'mvn deploy'
                }
            }
        }
    }
}