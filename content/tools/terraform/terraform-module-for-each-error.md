---
title: "[Solution] Terraform Module for_each Error"
description: "Fix Terraform module for_each errors when iterating over a module with for_each."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Module for_each errors occur when the iteration expression is invalid:

```
Error: Invalid for_each argument

The for_each value depends on resource attributes that cannot
be determined until apply.
```

## Common Causes

- for_each depends on computed values.
- Input map contains null or empty values.

## How to Fix

**Use variables with known values:**

```hcl
module "vpc" {
  source     = "../modules/vpc"
  for_each = var.environments
  name     = each.key
}

variable "environments" {
  type = map(object({
    cidr = string
  }))
  default = {
    prod = { cidr = "10.0.0.0/16" }
    dev  = { cidr = "10.1.0.0/16" }
  }
}
```

## Examples

```hcl
module "vpc" {
  for_each = {
    prod = "10.0.0.0/16"
    dev  = "10.1.0.0/16"
  }
  source     = "../modules/vpc"
  cidr_block = each.value
}
```
