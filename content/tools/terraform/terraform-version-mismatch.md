---
title: "[Solution] Terraform Version Mismatch"
description: "Fix Terraform version mismatch errors when your CLI version is incompatible with the configuration."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Version mismatch errors occur when your Terraform CLI version is incompatible:

```
Error: Terraform CLI version 1.3.0 is incompatible with state
format version 4 (written by Terraform 1.5.0).
Please upgrade Terraform to at least version 1.5.0.
```

## Common Causes

- State file was created with a newer Terraform version.
- Configuration uses features from a newer version.
- CI/CD pipeline uses a different version.

## How to Fix

**Upgrade Terraform:**

```bash
# Using tfenv
tfenv install latest
tfenv use latest
terraform version
```

**Pin version in CI/CD:**

```yaml
- uses: hashicorp/setup-terraform@v3
  with:
    terraform_version: "1.7.0"
```

**Check required version:**

```hcl
terraform {
  required_version = ">= 1.5.0"
}
```

## Examples

```hcl
terraform {
  required_version = ">= 1.5.0, < 2.0.0"
}
```
