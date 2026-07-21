---
title: "[Solution] AZURE App Service Plan"
description: "AppServicePlanError for plans."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `App Service Plan` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Plan name taken
- SKU not available
- Region capacity limit

## How to Fix

### List plans

```bash
az appservice plan list -g myRG
```

## Examples

- Example scenario: plan name taken
- Example scenario: sku not available
- Example scenario: region capacity limit

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
