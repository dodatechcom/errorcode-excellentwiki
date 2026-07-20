---
title: "[Solution] Terraform Plan Does Not Match"
description: "Fix Terraform plan does not match errors when actual resource state differs from the plan."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Plan mismatch errors occur during apply when reality differs from the plan:

```
Error: Provider produced inconsistent result after apply

When applying changes to aws_instance.example, provider
produced an unexpected new value: attribute "ami" changed.
```

## Common Causes

- Another process modified the resource between plan and apply.
- Cloud provider auto-modified attributes.

## How to Fix

**Retry the apply:**

```bash
terraform apply
```

**Use `-refresh-only`:**

```bash
terraform plan -refresh-only
```

**Add lifecycle ignore:**

```hcl
resource "aws_instance" "example" {
  ami = var.ami_id

  lifecycle {
    ignore_changes = [tags]
  }
}
```

## Examples

```hcl
lifecycle {
  ignore_changes = [tags, user_data]
}
```
