---
title: "[Solution] AZURE Helm Deployment"
description: "HelmError for Helm charts."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Helm Deployment` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Chart not found
- Release already exists
- Values file malformed

## How to Fix

### List releases

```bash
helm list
```

## Examples

- Example scenario: chart not found
- Example scenario: release already exists
- Example scenario: values file malformed

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
