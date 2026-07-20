---
title: "[Solution] Terraform Output Dependency Missing"
description: "Fix Terraform output dependency missing errors when outputs reference non-existent resources."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Output dependency missing errors occur when outputs reference missing resources:

```
Error: Reference to undeclared resource

Output "endpoint" references "aws_db_instance.main" which
has not been declared.
```

## Common Causes

- Resource was removed from configuration.

## How to Fix

**Use module outputs properly:**

```hcl
output "endpoint" {
  value = module.database.endpoint
}
```

**Add explicit dependency:**

```hcl
output "endpoint" {
  value     = aws_db_instance.main.endpoint
  depends_on = [aws_db_instance.main]
}
```

## Examples

```hcl
output "vpc_id" {
  value     = module.vpc.vpc_id
  depends_on = [module.vpc]
}
```
