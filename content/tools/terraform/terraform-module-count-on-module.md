---
title: "[Solution] Terraform Module Count On Module"
description: "Fix Terraform module count on module errors when using count with module blocks."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Module count errors occur when the `count` expression is invalid:

```
Error: Invalid count argument

The "count" value for module "vpc" depends on resource
attributes that cannot be determined until apply.
```

## Common Causes

- Count expression depends on computed values.
- Variable used in count is not known at plan time.

## How to Fix

**Use boolean variables:**

```hcl
module "vpc" {
  source     = "../modules/vpc"
  count      = var.create_vpc ? 1 : 0
  cidr_block = var.vpc_cidr
}
```

## Examples

```hcl
variable "create_vpc" {
  type    = bool
  default = true
}

module "vpc" {
  source = "../modules/vpc"
  count  = var.create_vpc ? 1 : 0
}
```
