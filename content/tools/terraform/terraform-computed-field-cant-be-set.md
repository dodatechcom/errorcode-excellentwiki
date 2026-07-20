---
title: "[Solution] Terraform Computed Field Cant Be Set"
description: "Fix Terraform computed field can't be set errors when trying to assign values to read-only attributes."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Computed field errors occur when trying to set a read-only attribute:

```
Error: Invalid attribute in config

The attribute "arn" is computed by the provider and cannot be
set in configuration.
```

## Common Causes

- Trying to set a provider-computed value.
- Copying values from state output into config.

## How to Fix

**Remove the computed attribute:**

```hcl
# Wrong
resource "aws_instance" "web" {
  ami = "ami-123"
  arn = "arn:aws:ec2:..."  # computed, cannot set
}

# Correct
resource "aws_instance" "web" {
  ami = "ami-123"
}
```

## Examples

```hcl
output "instance_arn" {
  value = aws_instance.web.arn  # computed, valid to read
}
```
