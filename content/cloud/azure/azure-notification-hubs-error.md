---
title: "[Solution] Azure Notification Hubs Error — registration, tag, and PNS failures"
description: "Fix Azure Notification Hubs error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 149
---

Notification Hub errors involve device registration failures, tag expression issues, or platform notification service (PNS) authentication problems.

## Common Causes
- PNS credentials (APNS/FCM) expired or misconfigured
- Tag expression syntax invalid causing push delivery failures
- Device registration tokens stale after app reinstall
- Namespace capacity exceeded with too many registrations
- Notification hub not associated with correct namespace

## How to Fix
### Check notification hub status
```bash
az notification-hub show \
  --resource-group myResourceGroup \
  --namespace-name myNamespace \
  --name myNotificationHub \
  --query "provisioningState"
```

### Update APNS credentials
```bash
az notification-hub update \
  --resource-group myResourceGroup \
  --namespace-name myNamespace \
  --name myNotificationHub \
  --apns-credential '{"apnsCertificate":"myPfxContent","certificateKey":"myPassword","endpoint":"AppleProduction"}'
```

### List registrations
```bash
az notification-hub registration list \
  --resource-group myResourceGroup \
  --namespace-name myNamespace \
  --notification-hub-name myNotificationHub
```

### Send test notification
```bash
az notification-hub send \
  --resource-group myResourceGroup \
  --namespace-name myNamespace \
  --name myNotificationHub \
  --notification-format gcm \
  --message '{"data":{"title":"Test","body":"Hello World"}}'
```

## Examples
### Create notification hub
```bash
az notification-hub create \
  --resource-group myResourceGroup \
  --namespace-name myNamespace \
  --name myNotificationHub \
  --location eastus
```

### List PNS settings
```bash
az notification-hub show \
  --resource-group myResourceGroup \
  --namespace-name myNamespace \
  --name myNotificationHub \
  --query "apnsCredential"
```

## Related Errors
- {{< relref "/cloud/azure/azure-event-hub-error" >}}
- {{< relref "/cloud/azure/azure-key-vault-error" >}}
- {{< relref "/cloud/azure/azure-app-service-error" >}}
