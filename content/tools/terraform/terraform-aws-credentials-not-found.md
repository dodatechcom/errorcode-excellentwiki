---
title: "[Solution] Terraform AWS Credentials Not Found"
description: "Fix Terraform AWS credentials not found errors when AWS provider cannot authenticate."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

AWS credentials errors occur when the provider cannot find valid credentials:

```
Error: error configuring Terraform AWS Provider

no valid credential sources for Terraform AWS Provider found.
```

## Common Causes

- `AWS_ACCESS_KEY_ID` not set.
- `~/.aws/credentials` doesn't exist.
- IAM role not attached to EC2/ECS.
- SSO session expired.

## How to Fix

**Set environment variables:**

```bash
export AWS_ACCESS_KEY_ID="AKIA..."
export AWS_SECRET_ACCESS_KEY="..."
export AWS_DEFAULT_REGION="us-east-1"
```

**Configure AWS CLI:**

```bash
aws configure
```

**Use IAM roles (recommended):**

```hcl
provider "aws" {
  region = "us-east-1"
  # No credentials needed — uses instance role
}
```

## Examples

```bash
aws sts get-caller-identity
aws sso login --profile production
export AWS_PROFILE=production
```
