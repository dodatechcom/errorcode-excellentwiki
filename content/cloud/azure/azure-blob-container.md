---
title: "[Solution] AZURE Blob Container"
description: "BlobContainerError for containers."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Blob Container` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Container already exists
- Container name invalid
- Lease conflict

## How to Fix

### List containers

```bash
az storage container list
```

## Examples

- Example scenario: container already exists
- Example scenario: container name invalid
- Example scenario: lease conflict

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
