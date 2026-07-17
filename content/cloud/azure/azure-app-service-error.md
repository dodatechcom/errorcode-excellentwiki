---
title: "[Solution] Azure App Service Deployment Error"
description: "Fix Azure App Service deployment errors. Resolve web app deployment issues."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

An Azure App Service deployment error occurs when the application cannot be deployed to Azure App Service. This can be caused by configuration, code, or runtime issues.

## Common Causes

- Incorrect runtime stack or version
- Missing application settings or connection strings
- Deployment source misconfigured
- Application startup failure
- Insufficient App Service plan resources

## How to Fix

### Check App Service Status

```bash
az webapp show --name myapp --resource-group myRG --query 'state'
```

### Check Deployment Logs

```bash
az webapp log deployment show --name myapp --resource-group myRG
```

### Configure App Settings

```bash
az webapp config appsettings set --name myapp --resource-group myRG \
  --settings "DATABASE_URL=connection_string"
```

### Set Runtime Stack

```bash
az webapp config set --name myapp --resource-group myRG \
  --runtime "NODE:18-lts"
```

### Deploy from Local

```bash
az webapp deployment source config-local-git --name myapp --resource-group myRG
az webapp deployment source config --name myapp --resource-group myRG \
  --repo-url https://github.com/user/repo --branch main
```

## Examples

```bash
# Example 1: Runtime mismatch
# Application Error: The page cannot be displayed
# Fix: set correct runtime in App Service configuration

# Example 2: Missing settings
# Connection string not found
# Fix: add connection string in App Service settings
```

## Related Errors

- [Azure SQL Error]({{< relref "/cloud/azure/azure-sql-error" >}}) — SQL connection error
- [Azure Functions Error]({{< relref "/cloud/azure/azure-functions-error" >}}) — Functions error
