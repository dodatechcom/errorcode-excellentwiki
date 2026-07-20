---
title: "[Solution] Terraform Force Copy Warning"
description: "Fix Terraform force copy warning when backend configuration changes require state migration."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Force copy warnings occur when backend configuration changes:

```
Terraform has detected that the configuration specified for the
backend has changed, which may result in data being lost or
moved. Would you like to copy the existing state to the new backend?
```

## Common Causes

- Backend configuration changed.
- Moving from local to remote backend.
- Changing S3 bucket or key.

## How to Fix

**Review the changes carefully:**

```bash
terraform init -migrate-state
```

**Force copy if intentional:**

```bash
terraform init -migrate-state -force-copy
```

**Backup first:**

```bash
terraform state pull > state-backup.json
```

## Examples

```bash
# Safe migration workflow
terraform state pull > backup.json
terraform init -migrate-state
# Verify state
terraform state list
```
