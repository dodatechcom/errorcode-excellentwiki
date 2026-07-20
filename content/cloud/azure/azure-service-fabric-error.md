---
title: "[Solution] Azure Service Fabric Error — cluster, application, and service failures"
description: "Fix Azure Service Fabric error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 113
---

Service Fabric errors include cluster upgrade failures, application deployment rollbacks, or node health issues causing service unavailability.

## Common Causes
- Cluster certificate not properly rolled during upgrade
- Application health probe failing causing restart loops
- Node state stuck in Disabling or Disabled state
- Image store connection string invalid or expired
- Upgrade parameters causing too long of an upgrade domain walk

## How to Fix
### Check cluster health
```bash
az sf cluster show-upgrade \
  --cluster-name myCluster \
  --resource-group myResourceGroup
```

### List application health
```bash
az sf cluster get-application-health \
  --cluster-name myCluster \
  --resource-group myResourceGroup \
  --application-name myApp
```

### Rollback failed application upgrade
```bash
az sf cluster rollback-upgrade \
  --cluster-name myCluster \
  --resource-group myResourceGroup \
  --upgrade-domain 0
```

### Repair disabled nodes
```bash
az sf cluster node-remove \
  --cluster-name myCluster \
  --resource-group myResourceGroup \
  --node-name NodeType0_3
```

## Examples
### Deploy new application version
```bash
az sf application create \
  --cluster-name myCluster \
  --resource-group myResourceGroup \
  --application-name myApp \
  --application-type-version 2.0 \
  --application-parameters '{"param1":"value1"}'
```

### Check cluster nodes status
```bash
az sf cluster node list \
  --cluster-name myCluster \
  --resource-group myResourceGroup
```

## Related Errors
- {{< relref "/cloud/azure/azure-aks-error" >}}
- {{< relref "/cloud/azure/azure-key-vault-error" >}}
- {{< relref "/cloud/azure/azure-monitor-error" >}}
