---
title: "[Solution] Azure Functions Hosting Error"
description: "Resolve Azure Functions hosting plan errors preventing deployment and function execution."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Hosting errors occur when the underlying App Service plan or Consumption plan cannot allocate resources for the function app. This causes deployment failures and runtime errors.

## Common Causes

- App Service plan is scaled to maximum instances with no capacity available
- Consumption plan region has insufficient capacity for the requested SKU
- Function app is in a disabled state due to billing issues
- Hosting plan was deleted or moved while function app still references it

## How to Fix

### Check function app hosting plan status

```bash
az functionapp show \
  --name myFuncApp \
  --resource-group myRG \
  --query "{State:state,Plan:serverFarmId}"
```

### List available hosting plan SKUs

```bash
az functionapp list-skus \
  --location eastus
```

### Scale the hosting plan

```bash
az functionapp plan update \
  --name myPlan \
  --resource-group myRG \
  --sku S1
```

### Create a new hosting plan

```bash
az functionapp plan create \
  --name myNewPlan \
  --resource-group myRG \
  --location eastus \
  --sku B1
```

## Examples

- Function app reports `SiteDisabled` when the App Service plan has zero instances
- Deployment fails with `HostingPlanCapacityExceeded` during high-traffic periods
- Function app stops responding after the hosting plan was downgraded to a lower SKU

## Related Errors

- [Azure Functions Error]({{< relref "/cloud/azure/azure-functions-error" >}}) -- General Functions errors.
- [Azure App Service Error]({{< relref "/cloud/azure/azure-app-service-error" >}}) -- App Service issues.
