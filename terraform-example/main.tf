module "network" {
  source   = "./modules/vpc"
  vpc_cidr = var.vpc_cidr
}
