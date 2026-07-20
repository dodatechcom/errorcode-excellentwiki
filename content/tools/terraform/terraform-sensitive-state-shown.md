---
title: "[Solution] Terraform Sensitive State Shown"
description: "Fix Terraform sensitive state shown warnings when sensitive values appear in state output."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Sensitive state visibility warnings occur when sensitive data appears in state:

```
Warning: sensitive attribute "password" is displayed in plan output
because it was set in configuration.
```

## Common Causes

- Marked outputs as sensitive but referenced in other resources.
- Provider doesn't mark computed sensitive attributes.

## How to Fix

**Mark sensitive attributes:**

```hcl
variable "db_password" {
  type      = string
  sensitive = true
}
```

**Encrypt state at rest:**

```hcl
terraform {
  backend "s3" {
    encrypt = true
  }
}
```

## Examples

```hcl
output "api_key" {
  value     = var.api_key
  sensitive = true
}
```
