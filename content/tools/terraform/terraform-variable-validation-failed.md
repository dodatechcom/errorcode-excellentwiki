---
title: "[Solution] Terraform Variable Validation Failed"
description: "Fix Terraform variable validation failed errors when input doesn't pass validation."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Validation errors occur when variable values don't pass validation:

```
Error: Invalid value for variable "environment"

Variable "environment" must be one of ["dev", "staging", "prod"],
but got "test".
```

## Common Causes

- Input value doesn't meet validation criteria.
- Validation rule is too restrictive.

## How to Fix

**Use appropriate validation rules:**

```hcl
variable "environment" {
  type = string

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "instance_count" {
  type = number

  validation {
    condition     = var.instance_count > 0 && var.instance_count <= 100
    error_message = "Instance count must be between 1 and 100."
  }
}
```

## Examples

```hcl
variable "email" {
  type = string

  validation {
    condition     = can(regex("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", var.email))
    error_message = "Must be a valid email address."
  }
}
```
