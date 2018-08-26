terraform {
  backend "s3" {
    bucket = "ngip-private"
    key    = "ngip-base-prod.tfstate"
    region = "ap-southeast-1"
    encrypt = true
    acl = "private"
  }
}