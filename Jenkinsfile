pipeline {
    agent any

    //Found that parameters tag only working for python code for ansible you need to pass parameter using job
    /*parameters {
    string(name: 'BUCKET', defaultValue: 'TEST231nhy', description: '')
    string(name: 'REGION', defaultValue: 'ap-south-1', description: '')
    }*/


    stages {
       /*stage('s3 bucket create using python') {
            steps {
                echo 'S3 Bucket creation using python'
                sh 'python create_s3_bucket.py '
            }
        } */
        /*stage('s3 Bucket creation using ansible') {
            steps {
                echo 'S3 Bucket ${params.BUCKET} creation using ansible'
                sh 'ansible-playbook s3.yml -e "myBucketName=$BUCKET  myRegion=$REGION" '
            }*/
        stage('s3 Bucket creation using Terraform') {
            steps {
                echo 'S3 Bucket ${params.BUCKET} creation using terraform'
                // sh 'terraform init terraform' //only needed first time when you run project
                 sh 'terraform apply -auto-approve -var-file="terraform/custom.tfvars" terraform '
            }
        }
    }

}
