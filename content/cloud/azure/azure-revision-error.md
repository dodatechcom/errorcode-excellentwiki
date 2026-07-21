---
title: "[Solution] AZURE Revision Error"
description: "RevisionError for container revisions."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Revision Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Revision name not found
- Replicas failed to start
- Liveness probe failing

## How to Fix

### Show revisions

```bash
az containerapp revision list -g myRG -n myApp
```

## Examples

- Example scenario: revision name not found
- Example scenario: replicas failed to start
- Example scenario: liveness probe failing

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
