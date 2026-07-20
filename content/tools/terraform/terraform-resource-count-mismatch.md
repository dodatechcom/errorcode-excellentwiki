---
title: "[Solution] Terraform Resource Count Mismatch"
description: "Fix Terraform resource count mismatch errors when planned and actual resource counts diverge."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Resource count mismatch occurs when expected count doesn't match reality:

```
Error: Resource count mismatch

Plan to create 3 resources, but 2 exist in state.
```

## Common Causes

- Resources imported or deleted outside Terraform.
- `count` or `for_each` expressions changed.
- State file manually edited.

## How to Fix

**Refresh state:**

```bash
terraform plan -refresh-only
```

**Import orphaned resources:**

```bash
terraform import aws_instance.web i-0123456789abcdef0
```

**Use `moved` blocks for renames:**

```hcl
moved {
  from = aws_instance.old_name
  to   = aws_instance.new_name
}
```

## Examples

```hcl
resource "aws_instance" "web" {
  count = var.instance_count
}
```
