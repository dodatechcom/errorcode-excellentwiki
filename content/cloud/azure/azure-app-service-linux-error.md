---
title: "[Solution] Azure App Service Linux Error"
description: "Fix Azure App Service Linux-specific errors including container startup failures and runtime issues."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Linux App Service errors differ from Windows-based errors due to container-based hosting. Startup failures and runtime mismatches are common in Linux environments.

## Common Causes

- Docker image used by the app is not compatible with the App Service Linux plan
- Startup command is misconfigured or points to a missing file
- Required environment variables are not set in the application settings
- Application depends on native libraries not available in the Linux base image

## How to Fix

### Check app startup logs

```bash
az webapp log tail \
  --name myApp \
  --resource-group myRG
```

### Set startup command

```bash
az webapp config set \
  --name myApp \
  --resource-group myRG \
  --startup-file "python3.9 -m gunicorn --bind=0.0.0.0 --workers=4 app:app"
```

### Configure Linux-specific settings

```bash
az webapp config set \
  --name myApp \
  --resource-group myRG \
  --linux-fx-version "PYTHON|3.9"
```

### View container logs

```bash
az webapp log download \
  --name myApp \
  --resource-group myRG \
  --output 0.zip
```

## Examples

- App crashes on startup because the Dockerfile uses a base image not supported by App Service
- Startup command references a file path that does not exist in the deployed package
- Application works locally but fails on App Service because native Redis client is not installed

## Related Errors

- [Azure App Service Error]({{< relref "/cloud/azure/azure-app-service-error" >}}) -- General App Service errors.
- [Azure Container Registry Error]({{< relref "/cloud/azure/azure-container-registry-error" >}}) -- ACR issues.
