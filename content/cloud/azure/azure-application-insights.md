---
title: "[Solution] AZURE Application Insights"
description: "AppInsightsError for Application Insights."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Application Insights` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Component not found
- Instrumentation key invalid
- Daily cap limit hit

## How to Fix

### List components

```bash
az monitor app-insights component list -g myRG
```

## Examples

- Example scenario: component not found
- Example scenario: instrumentation key invalid
- Example scenario: daily cap limit hit

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
