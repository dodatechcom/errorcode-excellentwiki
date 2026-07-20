---
title: "[Solution] Terraform Cloud API Error"
description: "Fix Terraform Cloud API errors when TFC API calls fail."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

TFC API errors occur when the Terraform Cloud API returns errors:

```
Error: TFC API Error 422: Validation Failed

The request body contains invalid fields.
```

## Common Causes

- Invalid API request format.
- Missing required fields.
- Rate limiting.

## How to Fix

**Check API request format:**

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN"   -H "Content-Type: application/vnd.api+json"   https://app.terraform.io/api/v2/organizations/my-org/workspaces   -d '{"data":{"type":"workspaces","attributes":{"name":"test"}}}'   | jq .
```

**Handle rate limiting:**

```bash
# Add delay between requests
sleep 1
```

## Examples

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN"   https://app.terraform.io/api/v2/organizations/my-org | jq '.data.attributes'
```
