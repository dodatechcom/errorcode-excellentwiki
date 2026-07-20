---
title: "[Solution] Terraform Required Field Missing"
description: "Fix Terraform required field missing errors when a mandatory resource argument is omitted."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Missing required field errors occur when a resource lacks a mandatory argument:

```
Error: Missing required argument

The argument "ami" is required, but no definition was found.
```

## Common Causes

- Forgot to include a required argument.
- Module input variable not set.

## How to Fix

**Add the required argument:**

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
}
```

**Use variables with defaults:**

```hcl
variable "ami_id" {
  type    = string
  default = "ami-0c55b159cbfafe1f0"
}
```

## Examples

```hcl
resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_type
}
```
