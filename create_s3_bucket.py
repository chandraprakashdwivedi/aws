#!/usr/bin/python

# ------------------
# Create a single S3 bucket, enable vesioning, attach policy
# =======================================

import os
import sys
import boto3
import json

# Set up the arguments required
myBucketName = os.environ.get('BUCKET').lower()
myRegion = os.environ.get('REGION').lower()

# Create Policy
policy = {
    'Version': '2019-03-26',
    'Statement': [{
        "Sid": "DenyUnEncryptedObjectUploads",
        "Effect": "Deny",
        "Principal": {
            "AWS": "*"
        },
        "Action": "s3:PutObject",
        "Resource": "arn:aws:s3:::" + myBucketName + "/*",
        "Condition": {
            "StringNotEquals": {
                "s3:x-amz-server-side-encryption": "AES256"
            }
        }
    }]
}
bucketDenyStatement = json.dumps(policy, indent=2)


def printOutput(myPrint):
    print
    "------ " + myPrint + " ------"


def getAllBuckets():
    for bucket in s3_conn.buckets.all():
        print(bucket.name)


# Create bucket
def createBucket(myBucketName, myRegion):
    if myRegion == 'us-east-1':
        s3_conn.create_bucket(Bucket=myBucketName)
    else:
        s3_conn.create_bucket(
            Bucket=myBucketName,
            CreateBucketConfiguration={'LocationConstraint': myRegion})


# Enable versioning on bucket
def bucketVersioning(myBucketName):
    bucket_versioning = s3_conn.BucketVersioning(myBucketName)
    bucket_versioning.enable()
    printOutput("Bucket Versioning Status: " + bucket_versioning.status)


# Apply policy on bucket
def bucketPolicy(myBucketName):
    bucket_policy = s3_conn.BucketPolicy(myBucketName)
    bucket_policy.put(Policy=bucketDenyStatement)


# Setup logging
def bucketLogging(myBucketName):
    logBucket = accountName + "-s3logs"
    bucket_logging = s3_conn.BucketLogging(myBucketName)
    bucket_logging.put(
        BucketLoggingStatus={
            'LoggingEnabled': {
                'TargetBucket': logBucket,
                'TargetPrefix': myBucketName + "/",
            }
        }
    )


# Run Portion
if __name__ == "__main__":

    s3_conn = boto3.resource('s3')


# Create bucket
    printOutput("Creating Bucket: " + myBucketName)
    createBucket(myBucketName, myRegion)

# Enable bucket versioning
#bucketVersioning(myBucketName)

# Apply bucket policy to bucket
#bucketPolicy(myBucketName)

# Apply bucket logging policy
#bucketLogging(myBucketName)

# Print all buckets
#printOutput("List of all buckets")
    getAllBuckets()

