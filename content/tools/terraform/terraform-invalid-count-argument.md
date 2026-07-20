---
title: "[Solution] Terraform Invalid Count Argument"
description: "Fix Terraform invalid count argument errors when count is not a non-negative integer."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Invalid count errors occur when the `count` expression is not valid:

```
Error: Invalid count argument

The "count" argument can only be used with a non-negative integer
value. You provided a value of type string.
```

## Common Causes

- `count` expression returns a non-integer value.
- `count` references an undefined variable.
- `count` expression returns null.

## How to Fix

**Use `length()` for collections:**

```hcl
resource "aws_instance" "web" {
  count         = length(var.instance_names)
  ami           = var.ami_id
  instance_type = "t3.micro"
}
```

**Use conditional:**

```hcl
resource "aws_instance" "web" {
  count = var.create_instance ? 1 : 0
}
```

## Examples

```hcl
variable "create" {
  type    = bool
  default = true
}

resource "aws_s3_bucket" "example" {
  count  = var.create ? 1 : 0
  bucket = "my-bucket"
}
```
