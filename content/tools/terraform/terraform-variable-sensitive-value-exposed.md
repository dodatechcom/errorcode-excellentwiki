---
title: "[Solution] Terraform Variable Sensitive Value Exposed"
description: "Fix Terraform variable sensitive value exposed warnings when sensitive variables appear in output."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Sensitive value exposure warnings appear when sensitive variables appear in plain text:

```
Warning: Sensitive variable "db_password" is used in
non-sensitive output "connection_string".
```

## Common Causes

- Sensitive variable used in string interpolation.
- Variable passed to non-sensitive output.

## How to Fix

**Keep sensitive variables marked:**

```hcl
variable "db_password" {
  type      = string
  sensitive = true
}
```

**Mark outputs containing sensitive values:**

```hcl
output "connection_string" {
  value     = "postgres://admin:${var.db_password}@host/db"
  sensitive = true
}
```

## Examples

```hcl
variable "api_key" {
  type      = string
  sensitive = true
}

output "api_config" {
  value = {
    key = var.api_key
  }
  sensitive = true
}
```
