---
title: "[Solution] AZURE VM Size Unavailable"
description: "VMSizeNotAvailable for the requested VM size."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `VM Size Unavailable` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- VM size not available in this region
- Size deprecated or retired
- Generation 2 vs Gen 1 mismatch

## How to Fix

### List sizes

```bash
az vm list-sizes --location eastus
```

## Examples

- Example scenario: vm size not available in this region
- Example scenario: size deprecated or retired
- Example scenario: generation 2 vs gen 1 mismatch

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
