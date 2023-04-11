pipeline{
    agent any
    stages{
        stage('Stage 1: Checkout '){
            steps{
                echo '...::: Checkout Version :::....'
                //checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '9593124e-4a9b-494b-9cf6-5b4fbf6ce9de', url: 'https://github.com/jonathanbs9/python-pytest.git']])
                echo 'Python Version'
                bat 'python --version'
            }
        }
        stage('Stage 2: Build - Descarga de repositorio'){
            steps{
                echo '...::: Acá sería git clone ?  :::...'
                git credentialsId: '9593124e-4a9b-494b-9cf6-5b4fbf6ce9de', url: 'https://github.com/jonathanbs9/python-pytest.git'
            }
        }

        stage('Ejecución de Test'){
            steps{
                echo '...::::: Executing test & report generation :::::...'
                bat 'python -m  pytest -v test/test_accum.py --html=report.html'
            }
        }

        stage('Publicación de Reporte'){
            steps{
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: '', reportFiles: 'report.html', reportName: 'HTML Report', reportTitles: '', useWrapperFileDirectly: true])
            }
        }
    }
}