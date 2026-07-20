---
title: "[Solution] Terraform Module Variable Not Set"
description: "Fix Terraform module variable not set errors when required module variables are missing."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Module variable not set errors occur when a required variable has no value:

```
Error: Missing required argument

Module "vpc" requires argument "cidr_block" which was not provided.
```

## Common Causes

- Forgot to pass required variable to module.
- Variable in module has no default.

## How to Fix

**Pass the required variable:**

```hcl
module "vpc" {
  source     = "../modules/vpc"
  cidr_block = "10.0.0.0/16"
}
```

**Add defaults in the module:**

```hcl
variable "cidr_block" {
  type    = string
  default = "10.0.0.0/16"
}
```

## Examples

```hcl
module "vpc" {
  source     = "hashicorp/vpc/aws"
  cidr_block = var.vpc_cidr
  name       = "production"
}
```
