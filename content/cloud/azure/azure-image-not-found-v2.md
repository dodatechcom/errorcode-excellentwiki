---
title: "[Solution] AZURE Image Not Found"
description: "ImageNotFound for VM image."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Image Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Image name incorrect
- Image deleted
- Image in different resource group

## How to Fix

### List images

```bash
az image list
```

## Examples

- Example scenario: image name incorrect
- Example scenario: image deleted
- Example scenario: image in different resource group

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
