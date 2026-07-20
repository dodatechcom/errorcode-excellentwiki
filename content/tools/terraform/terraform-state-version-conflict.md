---
title: "[Solution] Terraform State Version Conflict"
description: "Fix Terraform state version conflict errors when state format versions don't match."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

State version conflict errors occur when the state format is incompatible:

```
Error: Unsupported state version

State format version 4 cannot be read by Terraform 1.3.0.
```

## Common Causes

- State written by newer Terraform version.
- Mixed Terraform versions in team environments.

## How to Fix

**Upgrade Terraform CLI:**

```bash
tfenv install 1.7.0
tfenv use 1.7.0
```

**Standardize team version:**

```hcl
terraform {
  required_version = ">= 1.5.0"
}
```

## Examples

```bash
cat terraform.tfstate | jq '.version'
tfenv install latest
```
