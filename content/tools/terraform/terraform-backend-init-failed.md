---
title: "[Solution] Terraform Backend Init Failed"
description: "Fix Terraform backend initialization failures when configuring remote state backends."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Backend init errors occur when Terraform cannot initialize the configured backend:

```
Error: Failed to get existing workspaces: S3 bucket does not exist.

The referenced bucket does not exist or you lack permission to access it.
```

## Common Causes

- Remote backend resource does not exist yet (chicken-and-egg problem).
- IAM permissions insufficient for the backend storage.
- Backend configuration has incorrect values.

## How to Fix

**Use the local backend for initial setup:**

```hcl
terraform {
  backend "local" {}
}
```

**Migrate to remote backend after initial apply:**

```bash
terraform init -migrate-state
```

**Create prerequisite resources first:**

```hcl
resource "aws_s3_bucket" "terraform_state" {
  bucket = "my-terraform-state"
}

resource "aws_dynamodb_table" "terraform_lock" {
  name         = "terraform-lock"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}
```

## Examples

```hcl
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-lock"
    encrypt        = true
  }
}
```
