---
title: "[Solution] Azure Functions — host not started"
description: "Fix Azure Functions host not started. Resolve Functions host startup and initialization errors."
cloud: ["azure"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["azure", "functions", "host", "not-started", "runtime", "cold-start"]
weight: 5
---

An Azure Functions host not started error means the Functions host runtime failed to initialize and cannot process triggers. All function apps on the affected instance are non-operational.

## What This Error Means

Azure Functions runs on a host process that manages the lifecycle of function apps, loads extensions, connects to trigger sources (Service Bus, Event Hub, timer), and dispatches invocations. When the host fails to start — due to configuration errors, missing dependencies, or initialization failures — the function app returns HTTP 503 and logs host startup errors. The error message typically shows `Host did not start` or `A host error has occurred` with the specific initialization failure.

## Common Causes

- Missing or invalid connection strings for triggers
- Function runtime version mismatch (v3 vs v4)
- Missing NuGet packages or extensions
- Invalid function.json or host.json configuration
- Application Insights instrumentation key is invalid
- Out-of-memory during host startup
- Custom extension bundle version not found

## How to Fix

### Check Function App Logs

```bash
az functionapp logs tail --name my-func --resource-group my-rg
```

### Check Host Status

```bash
az functionapp show --name my-func --resource-group my-rg \
  --query 'state'
```

### Restart Function App

```bash
az functionapp restart --name my-func --resource-group my-rg
```

### Check host.json Configuration

```json
{
  "version": "2.0",
  "extensionBundle": {
    "id": "Microsoft.Azure.Functions.ExtensionBundle",
    "version": "[4.*, 5.0.0)"
  },
  "logging": {
    "applicationInsights": {
      "samplingSettings": {
        "isEnabled": true
      }
    }
  }
}
```

### Verify Connection Strings

```bash
az functionapp config connection-string list \
  --name my-func --resource-group my-rg
```

### Check Runtime Version

```bash
az functionapp show --name my-func --resource-group my-rg \
  --query 'siteConfig.netFrameworkVersion'
az functionapp config appsettings list \
  --name my-func --resource-group my-rg \
  --query "[?name=='FUNCTIONS_WORKER_RUNTIME']"
```

### Update Extension Bundle

```json
{
  "extensionBundle": {
    "id": "Microsoft.Azure.Functions.ExtensionBundle",
    "version": "[4.0.0, 5.0.0)"
  }
}
```

### Check Application Insights

```bash
az functionapp config appsettings list \
  --name my-func --resource-group my-rg \
  --query "[?name=='APPINSIGHTS_INSTRUMENTATIONKEY']"
```

## Related Errors

- [Azure App Service Error]({{< relref "/cloud/azure/azure-app-service-error-v2" >}}) — 503 Service Unavailable
- [Azure Functions Error]({{< relref "/cloud/azure/azure-functions-error" >}}) — original Functions error
- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error-v2" >}}) — Lambda runtime error
