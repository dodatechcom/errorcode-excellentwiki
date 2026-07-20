---
title: "[Solution] Terraform Workspace To Non-existent Target"
description: "Fix Terraform workspace errors when moving or copying to a non-existent workspace."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

This error occurs when referencing a workspace that doesn't exist:

```
Error: Target workspace "deploy" does not exist

The workspace "deploy" referenced by state push does not exist.
```

## Common Causes

- Typo in target workspace name.
- Workspace not yet created.

## How to Fix

**Create the target workspace:**

```bash
terraform workspace new deploy
```

**Verify workspace list:**

```bash
terraform workspace list
```

## Examples

```bash
terraform workspace new deploy
terraform workspace select deploy
terraform init
```
