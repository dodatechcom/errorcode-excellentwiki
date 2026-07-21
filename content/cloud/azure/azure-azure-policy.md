---
title: "[Solution] AZURE Azure Policy"
description: "AzurePolicyError for policy assignments."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Azure Policy` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Assignment not found
- Policy definition invalid
- Scope conflict

## How to Fix

### List assignments

```bash
az policy assignment list
```

## Examples

- Example scenario: assignment not found
- Example scenario: policy definition invalid
- Example scenario: scope conflict

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
