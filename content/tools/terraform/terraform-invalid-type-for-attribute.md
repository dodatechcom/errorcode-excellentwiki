---
title: "[Solution] Terraform Invalid Type For Attribute"
description: "Fix Terraform invalid type for attribute errors when the wrong type is assigned."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Type mismatch errors occur when assigning the wrong type:

```
Error: Incorrect attribute type

On main.tf line 15, in resource "aws_instance" "web":
  15:   tags = "Name=web"

Attribute "tags" must be a map of string, not a string.
```

## Common Causes

- Passing a string where a map is expected.
- Wrong type in variable definition.

## How to Fix

**Convert types using functions:**

```hcl
resource "aws_instance" "web" {
  tags = {
    Name = "web"
  }
}
```

**Use `tomap()` or `tolist()`:**

```hcl
locals {
  tag_map = tomap({ Name = "web", Environment = "prod" })
}
```

## Examples

```hcl
resource "aws_instance" "web" {
  instance_type = "t3.micro"
  ami           = "ami-12345"
  tags = {
    Name = "web"
  }
}
```
