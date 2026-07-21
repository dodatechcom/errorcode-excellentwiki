---
title: "[Solution] AZURE HTTP Trigger"
description: "HTTPTriggerError for HTTP functions."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `HTTP Trigger` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Authorization level invalid
- Route template invalid
- Method not allowed

## How to Fix

### Invoke function

```bash
az functionapp show -n myFuncApp -g myRG
```

## Examples

- Example scenario: authorization level invalid
- Example scenario: route template invalid
- Example scenario: method not allowed

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
