---
title: "[Solution] Terraform Cloud Policy Check Failed"
description: "Fix Terraform Cloud policy check failed errors when Sentinel policies reject the plan."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Policy check failures occur when Sentinel policies block the run:

```
Error: Policy check failed

The following policies failed:
- enforce-mandatory-tags: Resource missing required tags
```

## Common Causes

- Resource missing required tags.
- Instance type not in allowed list.
- Region restriction violated.

## How to Fix

**Fix the configuration to pass policies:**

```hcl
resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_type

  tags = {
    Environment = "production"
    Team        = "platform"
    CostCenter  = "12345"
  }
}
```

## Examples

```hcl
tags = {
  Environment = "production"
  ManagedBy   = "terraform"
  CostCenter  = var.cost_center
}
```
