pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/balu9493/projectFinal.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'C:\\Python311\\python.exe -m pip install --upgrade pip'
                bat 'C:\\Python311\\Scripts\\pip.exe install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'C:\\Python311\\python.exe -m pytest tests/'
            }
        }
    }
}
