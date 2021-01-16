locals {

  az_count = length(data.aws_availability_zones.available.names)

}
locals {
  suffix_add = ceil(log(local.az_count * 2, 2))
}

locals {
  public_cidr_list = [for cnt in range(local.az_count) :
    cidrsubnet(var.vpc_cidr, local.suffix_add, cnt)
  ]
}

locals {
  private_cidr_list = [for cnt in range(local.az_count) :
    cidrsubnet(var.vpc_cidr, local.suffix_add, cnt + local.az_count)
  ]
}
