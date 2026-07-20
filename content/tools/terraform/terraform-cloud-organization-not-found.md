---
title: "[Solution] Terraform Cloud Organization Not Found"
description: "Fix Terraform Cloud organization not found errors when the organization doesn't exist."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

TFC organization not found errors occur when referencing a non-existent org:

```
Error: Organization not found

The organization "my-org" does not exist or you do not
have permission to access it.
```

## Common Causes

- Organization name is incorrect.
- Organization was deleted.
- User not a member of the organization.

## How to Fix

**Verify organization name:**

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN"   https://app.terraform.io/api/v2/organizations/my-org | jq '.data.attributes.name'
```

**Check organization membership:**

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN"   https://app.terraform.io/api/v2/organizations/my-org/users | jq '.data[].attributes.username'
```

## Examples

```hcl
terraform {
  cloud {
    organization = "my-correct-org"
    workspaces {
      name = "my-workspace"
    }
  }
}
```
