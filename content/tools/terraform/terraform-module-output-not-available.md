---
title: "[Solution] Terraform Module Output Not Available"
description: "Fix Terraform module output not available errors when referencing a non-existent module output."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Module output not available errors occur when referencing a missing output:

```
Error: Reference to undeclared output

Module "vpc" does not output "subnet_ids". Available outputs:
"vpc_id", "cidr_block"
```

## Common Causes

- Output name typo in the module.
- Module was updated and output was removed.

## How to Fix

**Check available module outputs:**

```bash
cat modules/vpc/outputs.tf
```

**Use correct output name:**

```hcl
output "subnet_ids" {
  value = module.vpc.vpc_id
}
```

## Examples

```hcl
output "vpc_id" {
  value = module.vpc.vpc_id
}
```
