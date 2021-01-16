provider "aws" {
  region                  = var.aws_region
  shared_credentials_file = "/readonly/.aws/creds"
  # Terraform first will check environment variables (AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY) and if profile is defined then check in default location ~/.aws/credentials and if location is specified then in the speficied credentials file (if not found in default location)

  profile = var.aws_profile
}
