---
title: "[Solution] Azure App Service Deployment Credential Error"
description: "Fix Azure App Service deployment credential errors preventing Git and ZIP deploy operations."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Deployment credential errors occur when Git push or ZIP deploy fails because the publishing credentials are invalid or expired.

## Common Causes

- Deployment credentials have been rotated and local Git remote still uses old password
- SCM site credentials are disabled for security reasons
- Azure AD-based deployment credentials have expired refresh tokens
- Resource provider is not registered for the subscription

## How to Fix

### Reset deployment credentials

```bash
az webapp deployment user set \
  --user-name myDeployUser \
  --password "NewSecurePass123!"
```

### Enable basic auth for publishing

```bash
az webapp config set \
  --name myApp \
  --resource-group myRG \
  --generic-configurations '{"scmType":"BasicAuthPublishingCredentials"}'
```

### Get the Git remote URL with new credentials

```bash
az webapp deployment source show \
  --name myApp \
  --resource-group myRG \
  --query "repoUrl"
```

### Configure local git deployment

```bash
az webapp deployment source config-local-git \
  --name myApp \
  --resource-group myRG
```

## Examples

- Git push fails with `401 Unauthorized` after credentials were rotated in the portal
- ZIP deploy fails because the SCM site has basic auth disabled
- Deployment works from the Azure portal but fails from CI/CD pipeline with expired credentials

## Related Errors

- [Azure App Service Error]({{< relref "/cloud/azure/azure-app-service-error" >}}) -- General App Service errors.
- [Azure App Settings]({{< relref "/cloud/azure/azure-app-settings" >}}) -- App configuration.
