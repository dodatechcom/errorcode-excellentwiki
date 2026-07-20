---
title: "[Solution] Terraform Workspace Name Invalid"
description: "Fix Terraform workspace name invalid errors when workspace name contains invalid characters."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Invalid workspace name errors occur when the name doesn't match requirements:

```
Error: Invalid workspace name "my staging"

Workspace names can only contain letters, numbers, hyphens,
and underscores.
```

## Common Causes

- Spaces in workspace name.
- Special characters not allowed.
- Name too long.

## How to Fix

**Use valid characters only:**

```bash
terraform workspace new my-staging
terraform workspace new my_staging
```

**Naming requirements:**

- Only letters, numbers, `-`, and `_`
- Max 64 characters
- Cannot start with `global` (reserved)

## Examples

```bash
terraform workspace new prod-us-east-1
terraform workspace new staging_2024
terraform workspace new feature-xyz
```
