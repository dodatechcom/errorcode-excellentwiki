---
title: "[Solution] Terraform Output Value Type Mismatch"
description: "Fix Terraform output value type mismatch errors when output type doesn't match declaration."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Type mismatch errors occur when the output value doesn't match its type:

```
Error: Incorrect output type

Output "instance_ids" is declared as list(string) but value
is of type list(number).
```

## Common Causes

- Output type declaration doesn't match actual value.

## How to Fix

**Correct the type or convert value:**

```hcl
output "instance_ids" {
  value = [for inst in aws_instance.web : inst.id]
}
```

**Use type conversion:**

```hcl
output "port" {
  value = tostring(aws_db_instance.main.port)
}
```

## Examples

```hcl
output "instance_ids" {
  type  = list(string)
  value = [for i in aws_instance.web : i.id]
}

output "endpoint" {
  type  = string
  value = aws_db_instance.main.endpoint
}
```
