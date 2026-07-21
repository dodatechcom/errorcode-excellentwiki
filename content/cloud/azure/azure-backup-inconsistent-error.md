---
title: "[Solution] Azure Backup Inconsistent Error"
description: "Fix Azure Backup restore failures caused by inconsistent or corrupted backup points."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Backup inconsistency errors prevent Azure Backup from restoring data to a consistent state. This can result in data loss or corrupted restores.

## Common Causes

- Application-consistent backup failed due to VSS writer errors
- Snapshot-based backup has disk corruption at the backup time
- Backup chain has missing incremental snapshots
- Recovery point is older than the retention period and has been cleaned up

## How to Fix

### List recovery points

```bash
az backup recoverypoint list \
  --resource-group myRG \
  --vault-name myVault \
  --container-name myContainer \
  --item-name myVM \
  --query "[].{Id:id,Time:properties.time,Type:properties.recoveryPointType}"
```

### Trigger an on-demand backup

```bash
az backup backup-now \
  --resource-group myRG \
  --vault-name myVault \
  --container-name myContainer \
  --item-name myVM \
  --recovery-point-type "AppConsistent"
```

### Restore from a recovery point

```bash
az backup restore restore-disks \
  --resource-group myRG \
  --vault-name myVault \
  --container-name myContainer \
  --item-name myVM \
  --recovery-point-id "recoveryPointId" \
  --storage-account-type Standard_LRS
```

### Check backup job status

```bash
az backup job list \
  --resource-group myRG \
  --vault-name myVault \
  --container-name myContainer \
  --query "[].{Name:operation,Status:status,StartTime:startTime}"
```

## Examples

- Backup job completes with `PartialBackup` status because one disk was unavailable
- Restore fails with `InconsistentRecoveryPoint` because the last backup was crash-consistent only
- VSS writer errors prevent application-consistent backup of SQL Server VM

## Related Errors

- [Azure Backup Error]({{< relref "/cloud/azure/azure-backup-error" >}}) -- General backup errors.
- [Azure Site Recovery Error]({{< relref "/cloud/azure/azure-site-recovery-error" >}}) -- DR issues.
