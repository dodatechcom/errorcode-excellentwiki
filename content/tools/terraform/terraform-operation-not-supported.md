---
title: "[Solution] Terraform Operation Not Supported"
description: "Fix Terraform operation not supported errors when the backend doesn't support the requested operation."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Operation not supported errors occur when the backend cannot perform the action:

```
Error: Operation not supported

The "remote" backend does not support "terraform state mv".
```

## Common Causes

- Using state commands with remote backend.
- Feature not supported by backend type.

## How to Fix

**Switch to local backend for state operations:**

```hcl
terraform {
  backend "local" {}
}
```

**Use `-migrate-state`:**

```bash
terraform init -migrate-state
```

## Examples

```bash
terraform init -migrate-state -backend-config="bucket=new-bucket"
```
