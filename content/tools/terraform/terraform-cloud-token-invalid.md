---
title: "[Solution] Terraform Cloud Token Invalid"
description: "Fix Terraform Cloud token invalid errors when authentication fails."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

TFC token invalid errors occur when the API token is not accepted:

```
Error: Unauthorized

The provided API token is invalid or has been revoked.
```

## Common Causes

- Token was revoked.
- Token expired.
- Wrong token for the organization.

## How to Fix

**Re-authenticate:**

```bash
terraform login app.terraform.io
```

**Generate new API token:**

1. Go to Terraform Cloud > User Settings > Tokens
2. Create a new API token
3. Set environment variable:

```bash
export TFE_TOKEN="new-api-token"
```

**Use organization-scoped token:**

```bash
export TFE_TOKEN="atlasv1-xxx"
export TFE_ORG="my-org"
```

## Examples

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN"   https://app.terraform.io/api/v2/users/me | jq '.data.attributes.username'
```
