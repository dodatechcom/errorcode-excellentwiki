---
title: "[Solution] Terraform Address Not Found"
description: "Fix Terraform address not found errors when referencing a non-existent resource address."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Address not found errors occur when referencing a resource that doesn't exist:

```
Error: Reference to undeclared resource

A managed resource "aws_instance" "web" has not been declared.
```

## Common Causes

- Resource was not created due to `count = 0`.
- Resource address typo.
- Resource defined in a different module.

## How to Fix

**Use conditional reference:**

```hcl
locals {
  web_ip = try(aws_instance.web[0].private_ip, "N/A")
}
```

## Examples

```hcl
locals {
  ip = try(aws_instance.web[0].private_ip, "not-created")
}
```
