---
title: "[Solution] Terraform State Not Found"
description: "Fix Terraform state not found errors when the state file doesn't exist at the expected location."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

State not found errors occur when Terraform cannot locate the state file:

```
Error: Backend initialization required

Backend configuration has changed since the last initialization.
```

## Common Causes

- First-time initialization with remote backend.
- State key/path changed in backend configuration.

## How to Fix

**Verify backend configuration:**

```hcl
terraform {
  backend "s3" {
    bucket = "my-bucket"
    key    = "prod/terraform.tfstate"
    region = "us-east-1"
  }
}
```

**Check if state exists:**

```bash
aws s3 ls s3://my-bucket/terraform.tfstate
```

## Examples

```bash
aws s3 ls s3://my-bucket/ --recursive | grep terraform
terraform init
```
