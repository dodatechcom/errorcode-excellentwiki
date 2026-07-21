---
title: "[Solution] AZURE Blob Trigger"
description: "BlobTriggerError for blob triggers."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Blob Trigger` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Blob container not found
- Connection string missing
- Blob lease conflict

## How to Fix

### Create container

```bash
az storage container create -n mycontainer
```

## Examples

- Example scenario: blob container not found
- Example scenario: connection string missing
- Example scenario: blob lease conflict

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
