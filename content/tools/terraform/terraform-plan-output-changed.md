---
title: "[Solution] Terraform Plan Output Changed"
description: "Fix Terraform plan output changed errors when the plan differs from a previous preview."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The plan output changed error occurs when a saved plan no longer matches:

```
Error: Plan output has changed since it was saved.
```

## Common Causes

- External changes to infrastructure outside Terraform.
- Configuration files modified between plan and apply.
- Data sources returning different values.

## How to Fix

**Re-run the plan:**

```bash
terraform plan -out=tfplan
```

**Use refresh-only mode:**

```bash
terraform plan -refresh-only
```

**Prevent external changes:**

```hcl
resource "aws_instance" "web" {
  lifecycle {
    prevent_destroy = true
  }
}
```

## Examples

```bash
terraform plan -out=tfplan && terraform apply tfplan
terraform plan -detailed-exitcode
```
