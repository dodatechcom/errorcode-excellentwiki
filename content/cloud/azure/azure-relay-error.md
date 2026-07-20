---
title: "[Solution] Azure Relay Error — hybrid-connection, listener, and auth failures"
description: "Fix Azure Relay error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 151
---

Azure Relay errors occur when hybrid connections fail to establish listeners, WCF relay endpoints reject connections, or SAS token authentication fails.

## Common Causes
- Listener not started or stopped unexpectedly on WCF relay
- SAS token key expired without regeneration
- Hybrid connection access rights not configured for client
- Namespace throttled due to excessive connection attempts
- On-premises firewall blocking outbound port 443 to Azure Relay

## How to Fix
### Check relay namespace status
```bash
az relay namespace show \
  --resource-group myResourceGroup \
  --name myRelayNamespace \
  --query "provisioningState"
```

### List hybrid connections
```bash
az relay hybrid-connection list \
  --resource-group myResourceGroup \
  --namespace-name myRelayNamespace \
  --query "[].{name:name, userMetadata:userMetadata}"
```

### Regenerate SAS key
```bash
az relay namespace key regenerate \
  --resource-group myResourceGroup \
  --namespace-name myRelayNamespace \
  --key-name RootManageSharedAccessKey
```

### Create WCF relay
```bash
az relay wcf-relay create \
  --resource-group myResourceGroup \
  --namespace-name myRelayNamespace \
  --name myWcfRelay \
  --relay-type NetTcp
```

## Examples
### Create hybrid connection
```bash
az relay hybrid-connection create \
  --resource-group myResourceGroup \
  --namespace-name myRelayNamespace \
  --name myHybridConnection \
  --requires-client-authorization true
```

### List authorization rules
```bash
az relay hybrid-connection authorization-rule list \
  --resource-group myResourceGroup \
  --namespace-name myRelayNamespace \
  --hybrid-connection-name myHybridConnection
```

## Related Errors
- {{< relref "/cloud/azure/azure-service-bus-error" >}}
- {{< relref "/cloud/azure/auth-failed" >}}
- {{< relref "/cloud/azure/azure-vnet-error" >}}
