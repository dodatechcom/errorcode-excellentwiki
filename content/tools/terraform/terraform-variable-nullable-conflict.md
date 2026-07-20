---
title: "[Solution] Terraform Variable Nullable Conflict"
description: "Fix Terraform variable nullable conflicts when null values conflict with type constraints."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Nullable conflicts occur when null is used with non-nullable types:

```
Error: Invalid value for variable "name"

Variable "name" is not nullable but received null value.
```

## Common Causes

- Variable is non-nullable but null is passed.
- Module passes null for required variable.

## How to Fix

**Use nullable = true (default):**

```hcl
variable "name" {
  type    = string
  default = "default-name"
}
```

**Handle null with conditionals:**

```hcl
resource "aws_instance" "web" {
  instance_type = var.instance_type != null ? var.instance_type : "t3.micro"
}
```

## Examples

```hcl
variable "environment" {
  type     = string
  default  = "dev"
  nullable = true
}

locals {
  env = var.environment != null ? var.environment : "dev"
}
```
