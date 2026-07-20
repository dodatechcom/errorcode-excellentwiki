---
title: "[Solution] Terraform Variable Type Constraint Error"
description: "Fix Terraform variable type constraint errors when the value doesn't match the type constraint."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Type constraint errors occur when a variable value doesn't match type:

```
Error: Invalid value for variable "ports"

Variable "ports" must be a list of numbers, but got
["80", "443"] which contains strings.
```

## Common Causes

- Input type doesn't match variable type.
- Variable type definition is wrong.

## How to Fix

**Use correct type definitions:**

```hcl
variable "ports" {
  type    = list(number)
  default = [80, 443]
}

variable "config" {
  type = object({
    name    = string
    port    = number
    enabled = bool
  })
}
```

**Convert types in calling code:**

```hcl
module "app" {
  source = "../modules/app"
  ports  = [for p in var.port_strings : tonumber(p)]
}
```

## Examples

```hcl
variable "instances" {
  type = map(object({
    type = string
    ami  = string
    tags = map(string)
  }))
}
```
