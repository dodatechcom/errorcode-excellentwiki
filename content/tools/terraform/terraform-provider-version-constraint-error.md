---
title: "[Solution] Terraform Provider Version Constraint Error"
description: "Fix Terraform provider version constraint errors when no version satisfies all constraints."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

This error occurs when provider version constraints cannot all be satisfied:

```
Error: Failed to install provider

Constraint versions for hashicorp/aws cannot be satisfied:
  - required: >= 4.0, < 5.0
  - required by module.vpc: >= 5.0
```

## Common Causes

- Multiple modules specify conflicting version ranges for the same provider.
- Pinned version no longer available on the registry.
- Version constraint syntax errors.

## How to Fix

**Align version constraints across modules:**

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0, < 6.0"
    }
  }
}
```

**Override module constraints in root:**

```bash
terraform init -upgrade
```

## Examples

```hcl
# Module A: version = ">= 4.0, < 5.0"
# Module B: version = ">= 5.0"
# Fix: update both to version = ">= 4.0, < 6.0"
```
