---
title: "[Solution] Terraform Resource Update Failed"
description: "Fix Terraform resource update failed errors when modifying an existing resource."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Resource update failures occur when Terraform cannot modify a resource:

```
Error: Error updating Security Group (sg-12345): InvalidGroupPerm

The rule you specified already exists in this security group.
```

## Common Causes

- Resource in a state that prevents modification.
- API rejects the update due to constraints.

## How to Fix

**Check current state:**

```bash
terraform state show aws_security_group.example
```

**Force replacement:**

```bash
terraform apply -replace=aws_security_group.example
```

## Examples

```hcl
resource "aws_security_group" "web" {
  name = "web-sg"

  lifecycle {
    create_before_destroy = true
  }
}
```
