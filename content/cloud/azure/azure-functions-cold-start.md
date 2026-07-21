---
title: "[Solution] Azure Functions Cold Start Error"
description: "Fix Azure Functions cold start latency issues causing timeouts and poor user experience."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Cold start errors occur when Azure Functions take too long to initialize after being idle. This can cause HTTP-triggered functions to time out before the first response.

## Common Causes

- Function app is configured with Consumption plan and not enough warm instances
- Heavy dependencies slow down the cold start process
- App insights initialization adds significant startup time
- Function runtime version is outdated and has known startup performance issues

## How to Fix

### Enable Premium plan for pre-warmed instances

```bash
az functionapp plan create \
  --name myPlan \
  --resource-group myRG \
  --location eastus \
  --sku EP1
```

### Configure always-ready instances

```bash
az functionapp plan update \
  --name myPlan \
  --resource-group myRG \
  --min-instance-count 1
```

### Enable pre-warmed instances in code

```json
{
  "version": "2.0",
  "extensions": {
    "http": {
      "routePrefix": "",
      "maxOutstandingRequests": 200
    }
  }
}
```

### Reduce function app startup time

```bash
az functionapp config set \
  --name myFuncApp \
  --resource-group myRG \
  --min-tls-version 1.2
```

## Examples

- HTTP trigger takes 10+ seconds to respond on first invocation after idle period
- Function app times out after 30 seconds during cold start with heavy NuGet packages
- Premium plan with EP1 reduces cold start to under 2 seconds consistently

## Related Errors

- [Azure Functions Error]({{< relref "/cloud/azure/azure-functions-error" >}}) -- General Functions errors.
- [Azure Functions Timeout]({{< relref "/cloud/azure/azure-functions-error-v2" >}}) -- Timeout configuration.
