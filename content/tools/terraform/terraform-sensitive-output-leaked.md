---
title: "[Solution] Terraform Sensitive Output Leaked"
description: "Fix Terraform sensitive output leaked warnings when sensitive output values are exposed."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Sensitive output leaks occur when a sensitive output value is displayed:

```
Warning: Output "db_password" is marked as sensitive, but
its value is shown because it is referenced elsewhere.
```

## Common Causes

- Sensitive output referenced in non-sensitive output.
- Sensitive value passed to `nonsensitive()`.

## How to Fix

**Keep sensitive outputs marked:**

```hcl
output "db_password" {
  value     = random_password.db.result
  sensitive = true
}
```

## Examples

```hcl
output "api_key" {
  value     = var.api_key
  sensitive = true
}
```
