---
title: "[Solution] Terraform Workspace List Error"
description: "Fix Terraform workspace list errors when listing available workspaces fails."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Workspace list errors occur when Terraform cannot enumerate workspaces:

```
Error: Error listing workspaces

AccessDenied: Access denied to workspace list endpoint
```

## Common Causes

- Backend permissions insufficient.
- Backend service unavailable.

## How to Fix

**Check backend permissions:**

```bash
aws s3 ls s3://my-bucket/env:/
```

**Use local backend for debugging:**

```hcl
terraform {
  backend "local" {}
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN"   "https://app.terraform.io/api/v2/organizations/my-org/workspaces" | jq
```
