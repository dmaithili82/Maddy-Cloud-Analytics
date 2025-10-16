resource "aws_vpc" "maddy_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name        = "maddy-vpc"
    Environment = "dev"
    ManagedBy   = "terraform"
    Project     = "Maddy-Cloud-Analytics"
  }
}
