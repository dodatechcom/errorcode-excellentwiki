---
title: "[Solution] Terraform Output Not Found"
description: "Fix Terraform output not found errors when referencing a non-existent output."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Output not found errors occur when referencing an output that doesn't exist:

```
Error: Reference to undeclared output

A named output "vpc_id" has not been declared in the root module.
```

## Common Causes

- Output was removed from configuration.
- Typo in output name.

## How to Fix

**Check available outputs:**

```bash
terraform output
```

**Declare the output:**

```hcl
output "vpc_id" {
  value = aws_vpc.main.id
}
```

**Use `try()` for optional outputs:**

```hcl
locals {
  vpc_id = try(module.vpc.vpc_id, "N/A")
}
```

## Examples

```bash
terraform output
terraform output -raw vpc_id
```
