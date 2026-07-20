---
title: "[Solution] Terraform Variable Default Type Mismatch"
description: "Fix Terraform variable default type mismatch errors when the default value doesn't match the type."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Default type mismatch errors occur when default value doesn't match type:

```
Error: Invalid default value for variable

The variable "instance_count" has type "number" but the
default value "three" is not a valid number.
```

## Common Causes

- Default value doesn't match declared type.
- String used where number is expected.

## How to Fix

**Use correct default types:**

```hcl
variable "instance_count" {
  type    = number
  default = 3  # not "three"
}

variable "tags" {
  type = map(string)
  default = {
    Environment = "production"
    ManagedBy   = "terraform"
  }
}
```

## Examples

```hcl
variable "enabled" {
  type    = bool
  default = true
}

variable "instance_type" {
  type    = string
  default = "t3.micro"
}
```
