
resource "aws_internet_gateway" igw {

    vpc_id = var.vpc_id

  # This configuration combines some "default" tags with optionally provided additional tags
  tags = merge(
    var.resource_tags,
    {
      Name = "igw-${var.resource_tags["project_name"]}"
    },
  )
}
