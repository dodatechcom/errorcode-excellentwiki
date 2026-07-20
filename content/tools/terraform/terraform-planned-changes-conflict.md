---
title: "[Solution] Terraform Planned Changes Conflict"
description: "Fix Terraform planned changes conflict errors when multiple changes target the same resource."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Planned changes conflict occurs when Terraform has contradictory operations:

```
Error: Planned changes conflict

Resource aws_instance.example is planned to be both created
and destroyed in the same plan.
```

## Common Causes

- `count` expression changes between plan iterations.
- Resource naming changed in configuration.

## How to Fix

**Use moved blocks:**

```hcl
moved {
  from = aws_instance.old
  to   = aws_instance.new
}
```

**Separate operations:**

```bash
terraform apply -destroy -target=aws_instance.old
terraform apply
```

## Examples

```bash
terraform plan 2>&1 | grep "will be"
```
