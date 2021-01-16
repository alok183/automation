module "vpc" {
  source        = "./modules/vpc"
  vpc_cidr      = var.vpc_cidr
  resource_tags = var.resource_tags
}

module "igw" {
  source        = "./modules/igw"
  vpc_id        = module.vpc.out-vpc-id
  resource_tags = var.resource_tags
}

module "subnets" {
  source            = "./modules/subnets"
  vpc_id            = module.vpc.out-vpc-id
  resource_tags     = var.resource_tags
  azs               = data.aws_availability_zones.available
  public_cidr_list  = local.public_cidr_list
  private_cidr_list = local.private_cidr_list
}
