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

        stage('Generate Test Data') {
            steps {
                bat 'C:\\Python311\\python.exe generate_test_data.py'
            }
        }

        stage('Prioritize Tests (ML)') {
            steps {
                bat 'C:\\Python311\\python.exe ml_prioritizer.py'
            }
        }

        stage('Run Tests') {
    steps {
        bat 'C:\\Python311\\python.exe -m pytest tests/'
      }
    }
  }
}
