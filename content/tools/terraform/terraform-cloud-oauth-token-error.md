---
title: "[Solution] Terraform Cloud OAuth Token Error"
description: "Fix Terraform Cloud OAuth token errors when VCS integration fails."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

OAuth token errors occur when TFC cannot authenticate with the VCS:

```
Error: OAuth token error

The OAuth token for VCS connection is invalid or expired.
```

## Common Causes

- OAuth token was revoked on VCS side.
- VCS app permissions changed.

## How to Fix

**Re-create OAuth token:**

1. Go to Terraform Cloud > Organization Settings > VCS Providers
2. Remove old connection
3. Create new OAuth token

**Update workspace VCS connection:**

```bash
curl -X PATCH   -H "Authorization: Bearer $TFE_TOKEN"   https://app.terraform.io/api/v2/workspaces/ws-id   -d '{"data":{"relationships":{"oauth-token":{"data":{"type":"oauth-tokens","id":"ot-new-id"}}}}}'
```

## Examples

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN"   https://app.terraform.io/api/v2/organizations/my-org/oauth-tokens | jq '.data[].id'
```
