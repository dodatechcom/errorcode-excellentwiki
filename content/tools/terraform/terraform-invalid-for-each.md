---
title: "[Solution] Terraform Invalid for_each"
description: "Fix Terraform invalid for_each errors when the for_each argument is not a valid map or set."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Invalid for_each occurs when the expression doesn't produce a valid map or set:

```
Error: Invalid for_each argument

for_each can only be used with a map or set of strings, or a
list of strings. You provided a value of type string.
```

## Common Causes

- Passing a string instead of a map/list.
- Data source returns a list of objects (not strings).
- Variable is null or empty.

## How to Fix

**Convert to a map with stable keys:**

```hcl
resource "aws_instance" "example" {
  for_each = { for inst in var.instances : inst.name => inst }
  ami           = each.value.ami
  instance_type = each.value.type
}
```

**Ensure correct type:**

```hcl
variable "instances" {
  type = map(object({
    ami  = string
    type = string
  }))
}
```

## Examples

```hcl
resource "aws_instance" "good" {
  for_each = {
    web    = "t3.micro"
    api    = "t3.small"
    worker = "t3.medium"
  }
  instance_type = each.value
}
```
