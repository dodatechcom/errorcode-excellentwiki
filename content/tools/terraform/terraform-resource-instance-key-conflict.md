---
title: "[Solution] Terraform Resource Instance Key Conflict"
description: "Fix Terraform resource instance key conflict errors when multiple instances share the same key."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Instance key conflicts occur when `for_each` creates duplicate keys:

```
Error: Duplicate resource instance key

Resource "aws_instance" has two instances with key "web".
Keys must be unique.
```

## Common Causes

- Input list has duplicate entries.
- Map keys collide after transformation.

## How to Fix

**Deduplicate input data:**

```hcl
locals {
  unique_instances = { for inst in var.instances : inst.name => inst }
}
```

## Examples

```hcl
variable "instances" {
  type = map(object({
    type = string
  }))
}
```
