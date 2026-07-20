---
title: "[Solution] Terraform Current Workspace Deleted"
description: "Fix Terraform current workspace deleted errors when the active workspace was removed."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

This error occurs when the currently selected workspace no longer exists:

```
Error: Current workspace "staging" no longer exists

The workspace has been deleted.
```

## Common Causes

- Workspace deleted by another user or automation.
- CI/CD pipeline deleted the workspace.

## How to Fix

**Switch to default workspace:**

```bash
terraform workspace select default
```

**Recreate the workspace:**

```bash
terraform workspace new staging
terraform init
```

## Examples

```bash
terraform workspace select default
terraform workspace new staging
terraform init -migrate-state
```
