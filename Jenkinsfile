pipeline {

    agent {
        label 'master'
    }


    options {
        timestamps()
    }

    stages {

        stage("Execute migrations") {

            steps {
                sh "python3 manage.py migrate"
            }
        }


        stage("Reload App") {

            steps {
                sh "sudo supervisorctl restart django-demo2"
            }
        }


    }
}
