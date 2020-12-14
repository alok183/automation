variable "aws_region" {
  description = "AWS region to launch servers."
  default     = "ap-northeast-1"
}

variable "aws_profile" {
  description = "AWS profile to Authenticate."
  default     = "alsh1"
}


variable "vpc_cidr" {
  default = "192.168.0.0/16"
}
