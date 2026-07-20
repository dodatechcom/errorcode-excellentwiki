---
title: "[Solution] Terraform Output Interpolation Error"
description: "Fix Terraform output interpolation errors when interpolating values in output strings."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Interpolation errors occur when string interpolation syntax is wrong:

```
Error: Invalid template interpolation

Expected a valid value for expression: ${aws_instance.web.ip}
- did you mean "private_ip"?
```

## Common Causes

- Typo in attribute name.
- Wrong interpolation syntax.

## How to Fix

**Use correct interpolation syntax:**

```hcl
output "connection_string" {
  value = "postgres://user:pass@${aws_db_instance.main.address}:5432/db"
}
```

**Use `format()`:**

```hcl
output "endpoint" {
  value = format("%s:%d", aws_db_instance.main.address, aws_db_instance.main.port)
}
```

## Examples

```hcl
output "instance_info" {
  value = "Instance ${aws_instance.web.id} is at ${aws_instance.web.private_ip}"
}
```
