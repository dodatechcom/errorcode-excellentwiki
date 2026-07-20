---
title: "[Solution] Terraform Workspace Not Found"
description: "Fix Terraform workspace not found errors when selecting a non-existent workspace."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Workspace not found errors occur when trying to select a workspace that doesn't exist:

```
Error: Workspace "production" not found.

Use "terraform workspace list" to see available workspaces.
```

## Common Causes

- Workspace was deleted.
- Typo in workspace name.

## How to Fix

**List available workspaces:**

```bash
terraform workspace list
```

**Create the workspace:**

```bash
terraform workspace new production
terraform workspace select production
```

## Examples

```bash
terraform workspace new staging
terraform workspace select staging
terraform workspace list
```
