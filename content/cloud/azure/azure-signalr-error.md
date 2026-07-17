---
title: "[Solution] Azure SignalR Connection Error"
description: "Fix Azure SignalR connection errors. Resolve SignalR real-time connectivity issues."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

An Azure SignalR connection error occurs when clients cannot establish real-time connections through Azure SignalR Service.

## Common Causes

- SignalR service is not running or misconfigured
- Access key is incorrect or expired
- Hub name does not match the client configuration
- Network proxy or firewall blocking WebSocket
- Client SDK version incompatible with service

## How to Fix

### Check Service Status

```bash
az signalr show --name mysignalr --resource-group myRG --query 'provisioningState'
```

### Get Connection String

```bash
az signalr key list --name mysignalr --resource-group myRG \
  --query 'primaryConnectionString'
```

### Restart Service

```bash
az signalr restart --name mysignalr --resource-group myRG
```

### Check Client Connection

```javascript
const connection = new signalR.HubConnectionBuilder()
  .withUrl("https://mysignalr.service.signalr.net/client/?hub=myhub", {
    accessTokenFactory: () => token
  })
  .build();

connection.start().catch(err => console.error(err));
```

### Check Network

```bash
curl -v https://mysignalr.service.signalr.net/client/negotiate?hub=myhub
```

## Examples

```javascript
// Example 1: Connection refused
// Failed to connect to SignalR service
// Fix: verify connection string and hub name

// Example 2: Authentication failed
// Negotiate token invalid
// Fix: generate valid access token
```

## Related Errors

- [Azure AD Error]({{< relref "/cloud/azure/azure-ad-error" >}}) — AD authentication error
- [Azure App Service Error]({{< relref "/cloud/azure/azure-app-service-error" >}}) — App Service error
