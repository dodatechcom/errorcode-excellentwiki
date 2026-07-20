---
title: "[Solution] Terraform EC2 Instance Not Found"
description: "Fix Terraform EC2 instance not found errors when referencing a non-existent EC2 instance."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

EC2 instance not found errors occur when referencing a deleted or non-existent instance:

```
Error: Error finding instance

no matching EC2 instance found
```

## Common Causes

- Instance was manually terminated.
- Wrong instance ID.
- Wrong region.

## How to Fix

**Check instance status:**

```bash
aws ec2 describe-instances --instance-ids i-0123456789abcdef0
```

**Use data source with filters:**

```hcl
data "aws_instances" "web" {
  filter {
    name   = "tag:Environment"
    values = ["production"]
  }

  filter {
    name   = "instance-state-name"
    values = ["running"]
  }
}
```

## Examples

```hcl
data "aws_instance" "web" {
  filter {
    name   = "tag:Name"
    values = ["web-server"]
  }

  filter {
    name   = "instance-state-name"
    values = ["running"]
  }
}
```
