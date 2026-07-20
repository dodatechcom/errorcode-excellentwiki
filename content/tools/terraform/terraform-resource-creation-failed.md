---
title: "[Solution] Terraform Resource Creation Failed"
description: "Fix Terraform resource creation failed errors during terraform apply."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Resource creation failed when Terraform cannot create a new resource:

```
Error: Error creating EC2 Instance: InvalidParameterValue

The value 't3.micro' for parameter instanceType is not valid.
```

## Common Causes

- Invalid parameter values.
- Insufficient permissions.
- Resource quotas exceeded.

## How to Fix

**Add retry logic with timeouts:**

```hcl
resource "aws_instance" "web" {
  instance_type = var.instance_type
  ami           = data.aws_ami.latest.id

  timeouts {
    create = "10m"
  }
}
```

## Examples

```hcl
data "aws_ami" "latest" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}
```
