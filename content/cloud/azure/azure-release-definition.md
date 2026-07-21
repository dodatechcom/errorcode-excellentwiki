---
title: "[Solution] AZURE Release Definition"
description: "ReleaseDefError for releases."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Release Definition` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Release already exists
- Artifact source not connected
- Stage validation failed

## How to Fix

### Create release

```bash
az pipelines release create --definition-id 1
```

## Examples

- Example scenario: release already exists
- Example scenario: artifact source not connected
- Example scenario: stage validation failed

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
