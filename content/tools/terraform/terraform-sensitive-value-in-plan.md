---
title: "[Solution] Terraform Sensitive Value In Plan"
description: "Fix Terraform sensitive value in plan errors when sensitive attributes appear in plan output."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Sensitive value warnings occur when sensitive data appears in plan output:

```
Warning: Value is sensitive

The value of output "db_password" is marked as sensitive.
```

## Common Causes

- Output marked as sensitive but referenced in plain text.
- Sensitive variable used in non-sensitive context.

## How to Fix

**Mark outputs as sensitive:**

```hcl
output "db_password" {
  value     = random_password.db.result
  sensitive = true
}
```

**Use `nonsensitive()` when needed:**

```hcl
output "db_endpoint" {
  value = nonsensitive(aws_db_instance.main.endpoint)
}
```

## Examples

```hcl
variable "api_key" {
  type      = string
  sensitive = true
}

output "connection_string" {
  value     = "postgres://user:${var.api_key}@host/db"
  sensitive = true
}
```
