---
title: "[Solution] AZURE Container Instance"
description: "ContainerInstanceError for container instances."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Container Instance` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Container group already exists
- CPU/memory quota exceeded
- Image pull failed

## How to Fix

### Show instance

```bash
az container show -n myCI -g myRG
```

## Examples

- Example scenario: container group already exists
- Example scenario: cpu/memory quota exceeded
- Example scenario: image pull failed

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
