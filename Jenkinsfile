pipeline {
  
    agent {
        label 'master'
    }
 
 
    options {
        timestamps()
        ansiColor("xterm")
    }
 
    stages {
    
        stage("Execute migrations") {
          		    
            steps {
                sh "python3 manage.py migrate"
            }
        }
 
        stage("Run Tests") { 
            		
            steps {
                sh "python3 manage.py test"
            }
        }

        stage("Reload App") { 
            		
            steps {
                sh "sudo supervisorctl restart django-master"
            }
        }
 
        
    }
}
