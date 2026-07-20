---
title: "[Solution] Terraform Unsupported Argument"
description: "Fix Terraform unsupported argument errors when an argument is not supported by the resource."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Unsupported argument errors occur when using an unsupported argument:

```
Error: Unsupported argument

An argument named "access_key" is not expected here.
```

## Common Causes

- Argument was removed in newer provider version.
- Mixing provider-level and resource-level arguments.

## How to Fix

**Remove or replace the argument:**

```hcl
# Wrong — "access_key" moved to provider
resource "aws_instance" "web" {
  access_key = "AKIA..."
}

# Correct — use provider block
provider "aws" {
  access_key = var.access_key
  secret_key = var.secret_key
  region     = "us-east-1"
}
```

## Examples

```hcl
provider "aws" {
  region     = var.region
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
}
```
