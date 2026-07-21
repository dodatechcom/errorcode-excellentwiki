---
title: "[Solution] AZURE Build Definition"
description: "BuildDefError for build pipelines."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Build Definition` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Build already exists with name
- Task group version invalid
- Variables not defined

## How to Fix

### List builds

```bash
az pipelines build list
```

## Examples

- Example scenario: build already exists with name
- Example scenario: task group version invalid
- Example scenario: variables not defined

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
