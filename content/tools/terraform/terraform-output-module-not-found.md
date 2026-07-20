---
title: "[Solution] Terraform Output Module Not Found"
description: "Fix Terraform output module not found errors when referencing a non-existent module output."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Output module not found errors occur when an output references a missing module:

```
Error: Reference to undeclared module

An undeclared module named "vpc" has been referenced.
```

## Common Causes

- Module was removed from configuration.
- Typo in module name.

## How to Fix

**Verify module exists:**

```bash
ls -la modules/vpc/
```

**Check module declaration:**

```hcl
module "vpc" {
  source = "../modules/vpc"
}
```

## Examples

```hcl
output "vpc_id" {
  value = module.vpc.vpc_id
}
```
