---
title: "[Solution] Terraform Workspace Already Exists"
description: "Fix Terraform workspace already exists errors when creating a workspace that already exists."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Workspace already exists errors occur when trying to create a duplicate:

```
Error: Workspace "staging" already exists.

A workspace with this name already exists.
```

## Common Causes

- Workspace was created previously.
- CI/CD pipeline creates workspace without checking.

## How to Fix

**Check if workspace exists first:**

```bash
terraform workspace list | grep staging
```

**Use conditional creation in scripts:**

```bash
if ! terraform workspace list | grep -q "staging"; then
  terraform workspace new staging
fi
terraform workspace select staging
```

## Examples

```bash
terraform workspace new staging 2>/dev/null || terraform workspace select staging
```
