---
title: "[Solution] Azure Notification Hub Push Error"
description: "Fix Azure Notification Hub push notification delivery failures for mobile applications."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Push notification errors prevent Notification Hub from delivering messages to mobile devices. This affects both Android and iOS notification channels.

## Common Causes

- Push notification credentials (APNs, FCM) have expired or been revoked
- Device registration token is stale and no longer valid
- Notification hub namespace has reached the daily push limit
- PNS-specific configuration is missing or incorrect

## How to Fix

### Check notification hub credentials

```bash
az notification-hub show \
  --name myHub \
  --namespace-name myNamespace \
  --resource-group myRG \
  --query "apnsCredential|gcmCredential"
```

### Update APNs credential

```bash
az notification-hub credential update-apns \
  --name myHub \
  --namespace-name myNamespace \
  --resource-group myRG \
  --apns-credential "{\"apnsCertificate\":\"base64cert\",\"certificateKey\":\"privateKey\",\"endpoint\":\"https://api.push.apple.com\"}"
```

### Test push notification

```bash
az notification-hub send \
  --name myHub \
  --namespace-name myNamespace \
  --resource-group myRG \
  --body "Test notification"
```

### List device registrations

```bash
az notification-hub device list \
  --name myHub \
  --namespace-name myNamespace \
  --resource-group myRG
```

## Examples

- iOS notifications fail with `InvalidProviderToken` because the APNs certificate expired
- Android notifications return `InvalidRegistration` because the FCM server key was rotated
- Push notifications work in sandbox but fail in production due to wrong APNs endpoint

## Related Errors

- [Azure Notification Hubs Error]({{< relref "/cloud/azure/azure-notification-hubs-error" >}}) -- General notification errors.
- [Azure App Service Error]({{< relref "/cloud/azure/azure-app-service-error" >}}) -- Backend issues.
