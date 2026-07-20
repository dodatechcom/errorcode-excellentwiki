---
title: "[Solution] Terraform State Serial Mismatch"
description: "Fix Terraform state serial mismatch errors when concurrent state modifications are detected."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

State serial mismatch errors occur when state has been modified since last read:

```
Error: State serial mismatch

The state has serial 45, but the last known serial is 44.
```

## Common Causes

- Multiple Terraform runs modifying the same state.
- State was manually edited.
- CI/CD and local CLI running simultaneously.

## How to Fix

**Refresh and re-run:**

```bash
terraform plan -refresh-only
terraform apply
```

**Use workspaces:**

```bash
terraform workspace new feature-x
terraform apply
```

## Examples

```bash
terraform state pull | jq '.serial'
```
