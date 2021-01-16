resource "aws_subnet" "public_subnet" {
  count = length(var.azs.names)
  vpc_id = var.vpc_id
  cidr_block = var.public_cidr_list[count.index]
  availability_zone = var.azs.names[count.index]
  map_public_ip_on_launch = true
  tags = merge(
    var.resource_tags,
    {
      Name = "public-subnet-${var.resource_tags["project_name"]}-${count.index}"
    },
  )
}

resource "aws_subnet" "private_subnet" {
  count = length(var.azs.names)
  vpc_id = var.vpc_id
  cidr_block = var.private_cidr_list[count.index]
  availability_zone = var.azs.names[count.index]
  map_public_ip_on_launch = true
  tags = merge(
    var.resource_tags,
    {
      Name = "private-subnet-${var.resource_tags["project_name"]}-${count.index}"
    },
  )
}