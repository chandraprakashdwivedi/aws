pipeline {
    agent any

    parameters {
    string(name: 'BUCKET', defaultValue: 'TEST231nhy', description: '')
    string(name: 'REGION', defaultValue: 'ap-south-1', description: '')
    }


    stages {
        stage('s3 bucket create') {
            steps {
                echo 'S3 Bucket creation step'
                sh 'python create_s3_bucket.py '
            }
        }
    }
}
