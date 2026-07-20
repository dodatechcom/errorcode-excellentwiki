---
title: "[Solution] Azure Bot Service Error — channel, registration, and authentication failures"
description: "Fix Azure Bot Service error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 139
---

Bot Service errors appear as channel connection failures, registration app not configured, or messaging endpoint returning non-200 responses.

## Common Causes
- Messaging endpoint URL not accessible or returning HTTP errors
- Bot registration app secret expired in Azure AD
- Channel (Teams/Slack) not properly configured with bot credentials
- App Service hosting bot not running or scaled to zero
- OAuth connection string misconfigured for SSO scenarios

## How to Fix
### Check bot registration
```bash
az bot show \
  --resource-group myResourceGroup \
  --name myBot \
  --query "properties.provisioningState"
```

### Update bot messaging endpoint
```bash
az bot update \
  --resource-group myResourceGroup \
  --name myBot \
  --endpoint "https://mybotservice.azurewebsites.net/api/messages"
```

### Create new bot registration
```bash
az bot create \
  --resource-group myResourceGroup \
  --name myBot \
  --endpoint "https://mybotservice.azurewebsites.net/api/messages" \
  --appid myAppId \
  --app-type MultiTenant
```

### List connected channels
```bash
az bot channel list \
  --resource-group myResourceGroup \
  --bot-name myBot \
  --query "[].{name:name, etag:etag}"
```

## Examples
### Connect Teams channel
```bash
az bot channel create \
  --resource-group myResourceGroup \
  --bot-name myBot \
  --channel-name MicrosoftTeams \
  --location global
```

### Check bot app settings
```bash
az webapp config appsettings list \
  --resource-group myResourceGroup \
  --name myBotApp \
  --query "[].{name:name, value:value}"
```

## Related Errors
- {{< relref "/cloud/azure/auth-failed" >}}
- {{< relref "/cloud/azure/azure-app-service-error" >}}
- {{< relref "/cloud/azure/azure-key-vault-error" >}}
