provider "aws" {
  region = "${var.myRegion}"
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
