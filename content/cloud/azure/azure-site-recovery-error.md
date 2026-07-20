---
title: "[Solution] Azure Site Recovery Error — replication, failover, and mobility service failures"
description: "Fix Azure Site Recovery error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 122
---

Site Recovery errors appear as replication not starting, mobility service installation failures, or failover operations that leave VMs in inconsistent state.

## Common Causes
- Mobility service agent not installed or version outdated
- Replication policy RPO threshold exceeded during initial sync
- Target storage account or VNet not in same region as recovery vault
- Source VM firewall blocking Site Recovery service endpoints
- Disk encryption incompatible with replication provider

## How to Fix
### Check replication status
```bash
az site-recovery protected-item list \
  --resource-group myResourceGroup \
  --vault-name myRecoveryVault \
  --fabric-name myFabric \
  --query "[].{name:name, protectionState:properties.replicationHealth, policyName:properties.policyName}"
```

### Enable protection for VM
```bash
az site-recovery protectable-item initialize \
  --resource-group myResourceGroup \
  --vault-name myRecoveryVault \
  --fabric-name myFabric \
  --container-name myContainer \
  --protectable-item-name myVM
```

### Trigger failover
```bash
az site-recovery failover \
  --resource-group myResourceGroup \
  --vault-name myRecoveryVault \
  --fabric-name myFabric \
  --container-name myContainer \
  --protected-item-name myVM \
  --provider-configuration input.json
```

### Install mobility service
```bash
az site-recovery recovery-services-provider register \
  --resource-group myResourceGroup \
  --vault-name myRecoveryVault \
  --fabric-name myFabric \
  --provider-name myProvider \
  --authentication-identity input.json \
  --resource-access-identity input.json
```

## Examples
### Test failover
```bash
az site-recovery test-failover \
  --resource-group myResourceGroup \
  --vault-name myRecoveryVault \
  --fabric-name myFabric \
  --container-name myContainer \
  --protected-item-name myVM
```

### Check failover readiness
```bash
az site-recovery recovery-plan show \
  --resource-group myResourceGroup \
  --vault-name myRecoveryVault \
  --name myRecoveryPlan
```

## Related Errors
- {{< relref "/cloud/azure/azure-backup-error" >}}
- {{< relref "/cloud/azure/azure-vm-error" >}}
- {{< relref "/cloud/azure/azure-storage-error" >}}
