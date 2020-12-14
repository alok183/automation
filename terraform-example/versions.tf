terraform {
  # NOTE see page https://www.terraform.io/downloads.html for terraform latest release
  required_version = ">= 0.14"

  required_providers {
    # NOTE: see page https://www.terraform.io/docs/providers/aws/guides/version-3-upgrade.html for version 3 release
    aws = ">= 3.21.0"
  }
}
