---
title: "[Solution] Terraform Workspace Delete Failed"
description: "Fix Terraform workspace delete failed errors when removing a workspace."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Workspace delete errors occur when Terraform cannot remove a workspace:

```
Error: Error deleting workspace "staging"

Cannot delete workspace with existing resources.
```

## Common Causes

- Workspace contains resources that must be destroyed first.
- Cannot delete the currently selected workspace.

## How to Fix

**Destroy resources first:**

```bash
terraform workspace select staging
terraform destroy
```

**Switch to default workspace before deleting:**

```bash
terraform workspace select default
terraform workspace delete staging
```

## Examples

```bash
terraform workspace select default
terraform workspace delete staging
```
