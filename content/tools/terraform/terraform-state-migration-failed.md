---
title: "[Solution] Terraform State Migration Failed"
description: "Fix Terraform state migration failed errors when migrating state between backends."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

State migration errors occur when moving state from one backend to another:

```
Error: Error migrating state

Error: terraform state pull failed: AccessDenied
```

## Common Causes

- Insufficient permissions on new backend.
- New backend resource doesn't exist.

## How to Fix

**Migrate manually:**

```bash
terraform state pull > terraform.tfstate
terraform init -migrate-state
terraform state push terraform.tfstate
```

**Ensure both backends are accessible:**

```bash
terraform state pull > /dev/null
aws s3 ls s3://new-bucket/terraform.tfstate
```

## Examples

```bash
terraform state pull > state-backup.json
terraform init -migrate-state -backend-config="bucket=new-bucket"
terraform state push state-backup.json
```
