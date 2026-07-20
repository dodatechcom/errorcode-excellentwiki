---
title: "[Solution] GitHub Actions Azure Login Failed"
description: "Fix GitHub Actions Azure login failures in CI workflow."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Azure login failures occur when the workflow cannot authenticate with Azure:

```
Error: Error: az login failed
```

## Common Causes

- Azure credentials not configured.
- Service principal expired.
- Tenant/subscription ID incorrect.

## How to Fix

**Use OIDC with Azure:**

```yaml
permissions:
  id-token: write
  contents: read
steps:
  - uses: azure/login@v2
    with:
      client-id: ${{ secrets.AZURE_CLIENT_ID }}
      tenant-id: ${{ secrets.AZURE_TENANT_ID }}
      subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
```

## Examples

```yaml
steps:
  - uses: azure/login@v2
    with:
      client-id: ${{ secrets.AZURE_CLIENT_ID }}
      tenant-id: ${{ secrets.AZURE_TENANT_ID }}
      subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
  - run: az webapp list --query "[].name"
```
