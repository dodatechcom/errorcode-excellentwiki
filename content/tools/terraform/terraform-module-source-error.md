---
title: "[Solution] Terraform Module Source Error"
description: "Fix Terraform module source errors when the module source URL or path is invalid."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Module source errors occur when Terraform cannot locate the module:

```
Error: Invalid module source address

"git::https://github.com/org/module.git?ref=v1.0" is not
a valid module source address.
```

## Common Causes

- Malformed source URL.
- Missing required parameters (ref, version).
- Local path doesn't exist.

## How to Fix

**Verify module source syntax:**

```hcl
# Registry
module "vpc" {
  source  = "hashicorp/vpc/aws"
  version = "~> 3.0"
}

# Git
module "vpc" {
  source = "git::https://github.com/org/module.git?ref=v1.0"
}

# Local
module "vpc" {
  source = "../modules/vpc"
}
```

## Examples

```hcl
module "vpc" {
  source  = "hashicorp/consul/aws"
  version = "0.1.0"
}
```
