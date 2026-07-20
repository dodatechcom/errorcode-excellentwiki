---
title: "[Solution] Terraform Workspace Select Failed"
description: "Fix Terraform workspace select failed errors when switching between workspaces."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Workspace select errors occur when switching to a different workspace fails:

```
Error: Error selecting workspace

Workspace "production" has uncommitted changes.
```

## Common Causes

- Uncommitted state changes.
- State lock held by another process.

## How to Fix

**Commit or discard changes:**

```bash
terraform plan -refresh-only
```

**Force-select workspace:**

```bash
terraform workspace select -force production
```

## Examples

```bash
terraform workspace select default
terraform plan -refresh-only
terraform workspace select production
terraform plan
```
