variable "instance_name" {
  description = "The name of the AWS instance to be created"
  type        = string
  default     = "Task-2"
}

variable "aws_region" {
  description = "The region of the resource"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "Type of the instance to be created"
  type        = string
  default     = "t2.micro"
}