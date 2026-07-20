---
title: "[Solution] Azure NetApp Files Error — volume, capacity, and policy failures"
description: "Fix Azure NetApp Files error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 119
---

NetApp Files errors involve volume provisioning failures, capacity pool exhaustion, or snapshot policy issues that impact data availability.

## Common Causes
- NetApp resource provider not registered in subscription
- Capacity pool size insufficient for requested volume quota
- Volume protocol mismatch (NFS vs SMB) with client mount
- Snapshot policy schedule overlapping causing I/O spikes
- Subnet delegation not configured for NetApp resource provider

## How to Fix
### Register NetApp resource provider
```bash
az provider register --namespace Microsoft.NetApp --wait
```

### Check capacity pool usage
```bash
az netappfiles pool list \
  --resource-group myResourceGroup \
  --account-name myNetAppAccount \
  --query "[].{name:name, size:coolAccessEnabled, serviceLevel:serviceLevel, poolId:id}"
```

### Create new volume
```bash
az netappfiles volume create \
  --resource-group myResourceGroup \
  --account-name myNetAppAccount \
  --pool-name myPool \
  --name myVolume \
  --service-level Standard \
  --usage-threshold 100 \
  --protocol-types NFSv3 \
  --subnet /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Network/virtualNetworks/myVNet/subnets/mySubnet
```

### Update volume snapshot policy
```bash
az netappfiles volume update \
  --resource-group myResourceGroup \
  --account-name myNetAppAccount \
  --pool-name myPool \
  --name myVolume \
  --snapshot-policy /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.NetApp/netAppAccounts/myAccount/snapshotPolicies/myPolicy
```

## Examples
### Create capacity pool
```bash
az netappfiles pool create \
  --resource-group myResourceGroup \
  --account-name myNetAppAccount \
  --name myPool \
  --service-level Premium \
  --size 4398046511104
```

### List all volumes
```bash
az netappfiles volume list \
  --resource-group myResourceGroup \
  --account-name myNetAppAccount
```

## Related Errors
- {{< relref "/cloud/azure/azure-storage-error" >}}
- {{< relref "/cloud/azure/azure-vnet-error" >}}
- {{< relref "/cloud/azure/azure-backup-error" >}}
