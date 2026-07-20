---
title: "[Solution] Terraform Output Value Not Available"
description: "Fix Terraform output value not available errors when output value cannot be determined."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Output value not available errors occur when output depends on uncreated resources:

```
Error: Output value not available

The output "instance_ip" depends on resource
"aws_instance.web" which has not been created yet.
```

## Common Causes

- Output references a resource with `count = 0`.
- Resource creation failed.

## How to Fix

**Use `try()` for safe reference:**

```hcl
output "instance_ip" {
  value = try(aws_instance.web[0].public_ip, "N/A")
}
```

## Examples

```hcl
output "db_endpoint" {
  value = try(aws_db_instance.main[0].endpoint, "pending")
}
```
