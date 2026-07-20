---
title: "[Solution] Terraform Module Version Not Found"
description: "Fix Terraform module version not found errors when a specific version doesn't exist."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Module version not found errors occur when the requested version doesn't exist:

```
Error: Failed to download module

Could not find module version "2.0.0" for module "vpc".
Available: 1.0.0, 1.1.0, 1.2.0
```

## Common Causes

- Typo in version number.
- Version was yanked from registry.

## How to Fix

**Relax version constraints:**

```hcl
module "vpc" {
  source  = "hashicorp/vpc/aws"
  version = "~> 1.0"  # allows 1.x.x
}
```

## Examples

```hcl
module "vpc" {
  source  = "hashicorp/vpc/aws"
  version = ">= 1.0, < 2.0"
}
```
