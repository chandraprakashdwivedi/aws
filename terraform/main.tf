provider "aws" {
  region = "${var.myRegion}"
#  assume_role {
#  role_arn = "arn:aws:iam::12345551111111:role/cross-account-ec2-access"
#}
}

resource "aws_s3_bucket" "example" {
  bucket = "${var.myBucketName}"
  acl = "private"
  
   versioning {
    enabled = true
  }

   tags {
    Name = "${var.myBucketTag}"
  }

}
