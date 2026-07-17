---
title: "Azure App Service: The Process Has Exited with Code"
description: "App Service: The process has exited with code — Fix Azure App Service startup and crash errors."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

The `The process has exited with code` error occurs when the application process inside Azure App Service crashes or exits unexpectedly. The exit code indicates the reason — non-zero codes indicate failure, with specific codes pointing to different causes.

## Common Causes

- Application startup failure (missing configuration, unhandled exception)
- Wrong startup command or stack configuration
- Application dependencies not installed or wrong version
- Memory limit exceeded causing OOM kill (exit code 137)
- Port conflict inside the container

## How to Fix

Check the App Service logs:

```bash
az webapp log tail --name my-app --resource-group my-rg
```

Download full logs:

```bash
az webapp log download --name my-app --resource-group my-rg
```

Check the startup command:

```bash
az webapp config show --name my-app --resource-group my-rg --query 'startupFile'
```

Set the correct startup command:

```bash
# For Node.js
az webapp config set \
  --name my-app \
  --resource-group my-rg \
  --startup-file "node server.js"

# For Python
az webapp config set \
  --name my-app \
  --resource-group my-rg \
  --startup-file "gunicorn myapp:app"

# For .NET
az webapp config set \
  --name my-app \
  --resource-group my-rg \
  --startup-file "dotnet MyApp.dll"
```

Check resource limits:

```bash
az webapp show \
  --name my-app \
  --resource-group my-rg \
  --query '{Sku:sku.name, MemoryLimit:siteConfig.linuxFxVersion}'
```

## Examples

- Exit code 1: application throws an unhandled exception during startup
- Exit code 137: application exceeds the 1.5GB memory limit on Basic tier
- Exit code 3: application startup command is wrong — `dotnet` cannot find the DLL

## Related Errors

- [Azure Disk Error]({{< relref "/cloud/azure/disk-error" >}}) — disk I/O failure.
- [Azure Storage Error]({{< relref "/cloud/azure/storage-error" >}}) — storage account issues.
- [AWS Lambda Error]({{< relref "/cloud/aws/lambda-error" >}}) — AWS Lambda equivalent.
