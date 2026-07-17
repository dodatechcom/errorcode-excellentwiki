---
title: "[Solution] Azure App Service — 503 Service Unavailable"
description: "Fix Azure App Service 503 Service Unavailable. Resolve App Service scaling and startup issues."
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An Azure App Service 503 error means the application is temporarily unable to handle requests. The app may be starting up, restarting, scaled out with all instances unhealthy, or the platform is performing maintenance.

## What This Error Means

Azure App Service returns 503 when the platform cannot route traffic to healthy instances. This can occur during cold starts (first request after idle), during platform-initiated restarts, when all instances fail health checks, or when the app is being deployed. The error is platform-level, not application-level — the request never reaches your code. App Service's load balancer returns 503 because no healthy backend is available.

## Common Causes

- Application startup takes too long exceeding platform timeout
- All instances are unhealthy or failing health checks
- App is in a stopped state or crashed during startup
- Platform-initiated restart after OS updates
- Insufficient instance count (single instance failure)
- App Service Plan is at maximum capacity
- Connection string or configuration error preventing startup

## How to Fix

### Check App Status

```bash
az webapp show --name my-app --resource-group my-rg \
  --query '[state,defaultHostName]'
```

### Check App Logs

```bash
az webapp log tail --name my-app --resource-group my-rg
az webapp log download --name my-app --resource-group my-rg
```

### Restart the App

```bash
az webapp restart --name my-app --resource-group my-rg
```

### Check Instance Health

```bash
az webapp show --name my-app --resource-group my-rg \
  --query 'instances[].{id:id,state:state}'
```

### Increase Instance Count

```bash
az webapp update --name my-app --resource-group my-rg \
  --instance-count 3
```

### Scale Up App Service Plan

```bash
az appservice plan update --name my-plan --resource-group my-rg \
  --sku S2
```

### Enable Auto-Scaling

```bash
az monitor autoscale create \
  --resource-group my-rg \
  --resource my-app \
  --resource-type Microsoft.Web/sites \
  --condition "CpuPercentage > 80" \
  --min-count 2 --max-count 10
```

### Check Startup Command

```bash
az webapp config show --name my-app --resource-group my-rg \
  --query 'startupFile'
az webapp config set --name my-app --resource-group my-rg \
  --startup-file "dotnet MyApi.dll"
```

## Related Errors

- [Azure Functions Error]({{< relref "/cloud/azure/azure-functions-error-v2" >}}) — host not started
- [Azure VM Error]({{< relref "/cloud/azure/azure-vm-error-v2" >}}) — allocation failed
- [Nginx 503 Limit Request]({{< relref "/tools/nginx/nginx-limit-req-v2" >}}) — rate limiting
