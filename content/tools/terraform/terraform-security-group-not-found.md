---
title: "[Solution] Terraform Security Group Not Found"
description: "Fix Terraform security group not found errors when referencing a non-existent security group."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Security group not found errors occur when the referenced SG doesn't exist:

```
Error: Error: SecurityGroupNotFound

The security group 'sg-12345' does not exist in VPC 'vpc-abc123'
```

## Common Causes

- Security group was manually deleted.
- Wrong security group ID.
- Wrong VPC specified.

## How to Fix

**Create the security group in Terraform:**

```hcl
resource "aws_security_group" "web" {
  name   = "web-sg"
  vpc_id = aws_vpc.main.id
}
```

**Use data source for existing SG:**

```hcl
data "aws_security_group" "existing" {
  filter {
    name   = "group-name"
    values = ["web-sg"]
  }

  vpc_id = aws_vpc.main.id
}
```

## Examples

```hcl
resource "aws_security_group" "web" {
  name        = "web-sg"
  description = "Security group for web servers"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```
