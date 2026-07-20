---
title: "[Solution] Terraform Cloud Workspace Not Found"
description: "Fix Terraform Cloud workspace not found errors when the workspace doesn't exist."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

TFC workspace not found errors occur when referencing a non-existent workspace:

```
Error: Workspace "my-workspace" not found

The workspace could not be found in the organization.
```

## Common Causes

- Workspace was deleted.
- Wrong workspace name in configuration.
- Wrong organization configured.

## How to Fix

**Create the workspace:**

```bash
curl -X POST   -H "Authorization: Bearer $TFE_TOKEN"   -H "Content-Type: application/vnd.api+json"   https://app.terraform.io/api/v2/organizations/my-org/workspaces   -d '{"data":{"type":"workspaces","attributes":{"name":"my-workspace"}}}'
```

**Use Terraform to create workspace:**

```hcl
resource "tfe_workspace" "main" {
  name         = "my-workspace"
  organization = "my-org"
}
```

## Examples

```hcl
terraform {
  cloud {
    workspaces {
      name = "my-workspace"
    }
  }
}
```
