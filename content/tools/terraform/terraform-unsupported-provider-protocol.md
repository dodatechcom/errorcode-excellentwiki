---
title: "[Solution] Terraform Unsupported Provider Protocol"
description: "Fix Terraform unsupported provider protocol errors when provider uses incompatible gRPC protocol."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Protocol version mismatch errors occur when the provider uses an unsupported gRPC protocol:

```
Error: Incompatible provider version

Provider "hashicorp/aws" uses protocol version 6, but this
version of Terraform only supports protocol version 5.
```

## Common Causes

- Terraform CLI is too old for the provider version.
- Mixed versions in CI/CD and local environments.

## How to Fix

**Upgrade Terraform CLI:**

```bash
tfenv install 1.7.0
tfenv use 1.7.0
```

**Pin provider to compatible version:**

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0, < 5.0"
    }
  }
}
```

## Examples

```bash
terraform version
tfenv install latest && tfenv use latest
```
