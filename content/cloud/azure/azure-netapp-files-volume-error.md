---
title: "[Solution] Azure NetApp Files Error"
description: "Fix Azure NetApp Files volume and pool provisioning failures for high-performance storage."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

NetApp Files errors occur when volume or capacity pool provisioning fails. This blocks high-performance NFS and SMB storage for enterprise workloads.

## Common Causes

- Capacity pool has insufficient provisioned size for the requested volume
- delegated subnet is not configured or has no available IP addresses
- Volume snapshot is consuming space and preventing new volume creation
- Cross-region replication is enabled but the target region has no peering

## How to Fix

### Check capacity pool status

```bash
az netappfiles pool show \
  --resource-group myRG \
  --account-name myAccount \
  --pool-name myPool \
  --query "{Size:size,Used:usageThreshold,State:provisioningState}"
```

### List volumes in a pool

```bash
az netappfiles volume list \
  --resource-group myRG \
  --account-name myAccount \
  --pool-name myPool \
  --query "[].{Name:name,Size:usageThreshold,State:provisioningState}"
```

### Create a volume

```bash
az netappfiles volume create \
  --resource-group myRG \
  --account-name myAccount \
  --pool-name myPool \
  --volume-name myVolume \
  --service-level Premium \
  --usage-threshold 107374182400 \
  --file-path mypath \
  --vnet myVNet \
  --subnet mySubnet \
  --protocol-types NFSv4.1
```

### Check subnet delegation

```bash
az network vnet subnet show \
  --vnet-name myVNet \
  --name mySubnet \
  --resource-group myRG \
  --query "delegations"
```

## Examples

- Volume creation fails with `InsufficientCapacity` because the pool is 95% full
- Subnet delegation is missing and volume cannot be provisioned
- Cross-region replication fails because the ANF account peering is not configured

## Related Errors

- [Azure Netapp Files Error]({{< relref "/cloud/azure/azure-netapp-files-error" >}}) -- General ANF errors.
- [Azure VNet Error]({{< relref "/cloud/azure/azure-vnet-error" >}}) -- VNet issues.
