variable "aws_region" {
  description = "AWS region to launch servers."
  default     = "ap-southeast-1"
}

variable "aws_profile" {
  description = "AWS profile to Authenticate."
  default     = "alsh1"
}


variable "vpc_cidr" {
  default = "192.168.0.0/16"
}

# variable "environment" {
#   description = "Name of the environment."
#   default = "prod01"

# }

# variable "project_name" {
#   description = "Name of the project."
#   default = "alsh-b2b"

# }

variable "resource_tags" {
  description = "Tags to set for all resources"
  type        = map(string)
  default = {
    "environment"  = "prod01"
    "project_name" = "alsh-b2b"
    "owner"        = "devops"

  }
}
