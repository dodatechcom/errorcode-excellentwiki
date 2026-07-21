---
title: "[Solution] AZURE Blob Not Found"
description: "BlobNotFound for storage blobs."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Blob Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Blob name incorrect
- Blob deleted
- Path wrong in container

## How to Fix

### List blobs

```bash
az storage blob list --container mycontainer
```

## Examples

- Example scenario: blob name incorrect
- Example scenario: blob deleted
- Example scenario: path wrong in container

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
