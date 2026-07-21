---
title: "[Solution] AZURE Service Connection"
description: "ServiceConnectionError for connections."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Service Connection` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Connection already exists
- Credentials expired
- Endpoint unreachable

## How to Fix

### List connections

```bash
az devops service-endpoint list
```

## Examples

- Example scenario: connection already exists
- Example scenario: credentials expired
- Example scenario: endpoint unreachable

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
