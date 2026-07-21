---
title: "[Solution] Azure Functions Deployment Error"
description: "Fix Azure Functions deployment failures caused by ZIP deploy, SCM, or package errors."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Deployment errors occur when Azure Functions cannot deploy the function package. This can happen with ZIP deploy, code-based deployment, or CI/CD pipelines.

## Common Causes

- Function package exceeds the maximum allowed size for the hosting plan
- Deployment slot is misconfigured and cannot receive new deployments
- Kudu SCM site is unreachable due to network restrictions or app settings
- Azure Functions runtime version mismatch between local and cloud environment

## How to Fix

### Deploy using ZIP deploy

```bash
az functionapp deployment source config-zip \
  --name myFuncApp \
  --resource-group myRG \
  --src ./publish.zip
```

### Check deployment status

```bash
functionapp deployment list-publishing-profiles \
  --name myFuncApp \
  --resource-group myRG
```

### Enable SCM site for debugging

```bash
az functionapp config set \
  --name myFuncApp \
  --resource-group myRG \
  --generic-configurations '{"scmType":"BasicAuthPublishingCredentials"}'
```

## Examples

- ZIP deploy fails with `PackageExceedsSizeLimit` for functions with large binaries
- Deployment succeeds but functions do not appear in the portal due to stale cache
- SCM site returns 403 Forbidden after enabling IP restrictions on the function app

## Related Errors

- [Azure Functions Error]({{< relref "/cloud/azure/azure-functions-error" >}}) -- General Functions errors.
- [Azure App Service Deployment]({{< relref "/cloud/azure/azure-app-service-error-v2" >}}) -- App Service deployment.
