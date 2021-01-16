# Network configuration

# VPC creation
resource "aws_vpc" "vpc" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  # This configuration combines some "default" tags with optionally provided additional tags
  tags = merge(
    var.resource_tags,
    {
      Name = "vpc-${var.resource_tags["project_name"]}"
    },
  )
}
