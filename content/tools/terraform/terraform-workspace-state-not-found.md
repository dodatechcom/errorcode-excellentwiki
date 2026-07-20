---
title: "[Solution] Terraform Workspace State Not Found"
description: "Fix Terraform workspace state not found errors when the workspace state file is missing."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Workspace state not found errors occur when state for a workspace is missing:

```
Error: State not found for workspace "staging"

The state file for workspace "staging" was not found.
```

## Common Causes

- Workspace was created but never initialized.
- State file was deleted from backend.

## How to Fix

**Initialize the workspace:**

```bash
terraform workspace select staging
terraform init
```

**Import resources into workspace:**

```bash
terraform workspace select staging
terraform import aws_instance.web i-0123456789
```

## Examples

```bash
aws s3 ls s3://my-bucket/env:/staging/terraform.tfstate
```
