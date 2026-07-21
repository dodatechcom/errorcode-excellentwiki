---
title: "[Solution] Azure Site Recovery Replication Error"
description: "Fix Azure Site Recovery replication failures that prevent disaster recovery protection."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Replication errors prevent Azure Site Recovery from replicating VM data to the secondary region. This leaves VMs unprotected during outages.

## Common Causes

- Replication policy has been modified or deleted after initial configuration
- Source VM has changed disk configuration since protection was enabled
- Network mapping does not connect to a valid target VNet
- Recovery services vault is in a different region than the source VM

## How to Fix

### Check replication status

```bash
az site-recovery protected-item list \
  --resource-group myRG \
  --vault-name myVault \
  --fabric-name myFabric \
  --query "[].{Name:name,ReplicationState:replicationState,ProtectionState:protectionState}"
```

### Enable replication

```bash
az site-recovery protected-item enable \
  --resource-group myRG \
  --vault-name myVault \
  --fabric-name myFabric \
  --protection-container-name myContainer \
  --name myVM \
  --policy-name myPolicy
```

### Check replication health

```bash
az site-recovery replication-recovery-plan list \
  --resource-group myRG \
  --vault-name myVault \
  --query "[].{Name:name,Status:status}"
```

### Re-protect after failover

```bash
az site-recovery replication-recovery-plan reprotect \
  --resource-group myRG \
  --vault-name myVault \
  --name myRecoveryPlan
```

## Examples

- Replication state shows `Failed` because the target VNet was deleted
- Replication health is Critical due to RPO limit exceeded
- Initial seeding takes longer than expected because the source VM has a 2 TB disk

## Related Errors

- [Azure Site Recovery Error]({{< relref "/cloud/azure/azure-site-recovery-error" >}}) -- General ASR errors.
- [Azure Replication Error]({{< relref "/cloud/azure/azure-replication-error" >}}) -- Replication issues.
