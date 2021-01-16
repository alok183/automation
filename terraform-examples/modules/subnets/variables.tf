variable "vpc_id" {}
variable "resource_tags" { type = map(string) }
variable "azs"  {}
variable "public_cidr_list" { type = list(string)}
variable "private_cidr_list" { type = list(string)}