terraform {
backend "s3" {
bucket = "my-terraform-state-bucket-amaka"
key = "env/dev/terraform.tfstate"
region = "eu-north-1"
encrypt = true
}
}
