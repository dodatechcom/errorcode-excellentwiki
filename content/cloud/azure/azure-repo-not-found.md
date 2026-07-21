---
title: "[Solution] AZURE Repo Not Found"
description: "RepoNotFound for Azure Repos."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Repo Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Repo name incorrect
- Deleted
- Not cloned

## How to Fix

### List repos

```bash
az repos list
```

## Examples

- Example scenario: repo name incorrect
- Example scenario: deleted
- Example scenario: not cloned

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
