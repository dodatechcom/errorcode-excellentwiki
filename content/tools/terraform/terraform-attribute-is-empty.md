---
title: "[Solution] Terraform Attribute Is Empty"
description: "Fix Terraform attribute is empty errors when referencing empty or null resource attributes."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

This error occurs when referencing an attribute that has no value:

```
Error: Attribute must not be empty

The attribute "arn" is empty, but was referenced by
resource "aws_instance" "example".
```

## Common Causes

- Referencing a computed attribute before resource is created.
- Data source returning empty or null values.
- Missing required argument.

## How to Fix

**Use `try()` or null checks:**

```hcl
locals {
  instance_arn = try(aws_instance.example.arn, "")
}
```

**Use conditional expressions:**

```hcl
output "instance_arn" {
  value = aws_instance.example.arn != null ? aws_instance.example.arn : "pending"
}
```

## Examples

```hcl
locals {
  safe_arn = try(aws_instance.example.arn, "unknown")
}
```
