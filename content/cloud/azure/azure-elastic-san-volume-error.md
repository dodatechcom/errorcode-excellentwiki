---
title: "[Solution] Azure Elastic SAN Error"
description: "Fix Azure Elastic SAN volume group and volume provisioning failures for block storage."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Elastic SAN errors prevent provisioning of high-performance block storage volumes. This affects VM and container workloads that need shared block storage.

## Common Causes

- Elastic SAN is not in a provisioned state and cannot create volumes
- Volume group does not have network access configured for the target VNet
- IOPS or throughput limits on the Elastic SAN are exceeded
- Encryption key from Key Vault is not accessible to the Elastic SAN

## How to Fix

### Check Elastic SAN status

```bash
az elastic-san show \
  --resource-group myRG \
  --elastic-san-name mySan \
  --query "properties.provisioningState"
```

### List volume groups

```bash
az elastic-san volume-group list \
  --resource-group myRG \
  --elastic-san-name mySan \
  --query "[].{Name:name,State:provisioningState}"
```

### Create a volume

```bash
az elastic-san volume create \
  --resource-group myRG \
  --elastic-san-name mySan \
  --volume-group-name myGroup \
  --volume-name myVolume \
  --size-gib 100 \
  --storage-target-type Iscsi \
  --initiator-iqn "iqn.2026-01.com.microsoft:myvm"
```

### Configure volume group network rules

```bash
az elastic-san volume-group update \
  --resource-group myRG \
  --elastic-san-name mySan \
  --volume-group-name myGroup \
  --network-acls virtual-network-rules "[{id:'/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Network/virtualNetworks/myVNet/subnets/mySubnet'}]"
```

## Examples

- Volume creation fails because the Elastic SAN is at maximum capacity
- Network rules block the VM from connecting to the Elastic SAN volume
- IOPS limit is reached and new volumes cannot be created with the requested performance tier

## Related Errors

- [Azure Managed Disk Error]({{< relref "/cloud/azure/azure-managed-disk" >}}) -- Disk issues.
- [Azure Storage Error]({{< relref "/cloud/azure/azure-storage-error" >}}) -- Storage errors.
