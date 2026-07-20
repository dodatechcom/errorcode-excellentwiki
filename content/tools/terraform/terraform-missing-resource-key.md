---
title: "[Solution] Terraform Missing Resource Key"
description: "Fix Terraform missing resource key errors when accessing a non-existent map key on a resource."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Missing resource key errors happen when accessing a map attribute that doesn't exist:

```
Error: Invalid index

This value does not have any attributes; you cannot index into
it using key "tags" on aws_instance.example.
```

## Common Causes

- Resource doesn't have the referenced attribute.
- Typo in attribute name.
- Accessing optional nested block that wasn't configured.

## How to Fix

**Use `try()` for safe access:**

```hcl
locals {
  name = try(aws_instance.example.tags.Name, "unnamed")
}
```

**Use `lookup()` with defaults:**

```hcl
locals {
  name = lookup(aws_instance.example.tags, "Name", "unnamed")
}
```

## Examples

```hcl
locals {
  environment = try(aws_instance.example.tags.Environment, "unknown")
}
```
