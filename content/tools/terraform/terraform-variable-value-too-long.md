---
title: "[Solution] Terraform Variable Value Too Long"
description: "Fix Terraform variable value too long errors when a variable exceeds maximum length."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Value too long errors occur when input exceeds length constraints:

```
Error: Invalid value for variable "instance_name"

The value exceeds the maximum length of 63 characters.
```

## Common Causes

- Generated name exceeds provider limits.
- Concatenation produces overly long strings.

## How to Fix

**Add validation for length:**

```hcl
variable "instance_name" {
  type = string

  validation {
    condition     = length(var.instance_name) <= 63
    error_message = "Instance name must be 63 characters or less."
  }
}
```

**Truncate names using functions:**

```hcl
locals {
  safe_name = substr(var.instance_name, 0, 63)
}

resource "aws_instance" "web" {
  tags = {
    Name = local.safe_name
  }
}
```

## Examples

```hcl
variable "name" {
  type = string

  validation {
    condition     = length(var.name) >= 3 && length(var.name) <= 63
    error_message = "Name must be between 3 and 63 characters."
  }
}
```
