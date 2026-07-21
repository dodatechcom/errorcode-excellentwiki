---
title: "[Solution] AZURE Kudu Error"
description: "KuduError for Kudu/SCM."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Kudu Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- SCM endpoint unreachable
- Auth token expired
- Deployment credential invalid

## How to Fix

### Get publish profile

```bash
az webapp deployment list-publishing-profiles -g myRG -n myApp
```

## Examples

- Example scenario: scm endpoint unreachable
- Example scenario: auth token expired
- Example scenario: deployment credential invalid

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
