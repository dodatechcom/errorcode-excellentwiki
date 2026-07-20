---
title: "[Solution] Azure Backup Error — vault, policy, restore, and agent failures"
description: "Fix Azure Backup error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 121
---

Backup errors occur when vault cannot protect resources, recovery points are corrupted, or restore operations fail due to agent misconfiguration.

## Common Causes
- Recovery Services vault not in same region as protected resource
- Backup policy schedule exceeding retention period limits
- MARS agent on-premises not updated to latest version
- Resource moved to different subscription without vault reconfiguration
- Soft-delete retention blocking vault deletion

## How to Fix
### Check backup job status
```bash
az backup job list \
  --resource-group myResourceGroup \
  --vault-name myRecoveryVault \
  --query "[].{name:name, status:properties.status, operation:properties.operation}"
```

### Create backup policy
```bash
az backup policy create \
  --resource-group myResourceGroup \
  --vault-name myRecoveryVault \
  --name myBackupPolicy \
  --policy '{"backupManagementType":"AzureIaasVM","schedulePolicy":{"schedulePolicyType":"SimpleSchedulePolicy","scheduleRunFrequency":"Daily","scheduleRunTimes":["2023-01-01T02:00:00+00:00"]},"retentionPolicy":{"retentionPolicyType":"LongTermRetentionPolicy","dailySchedule":{"retentionTimes":["2023-01-01T02:00:00+00:00"],"retentionDuration":{"count":30,"durationType":"Days"}}}}'
```

### Enable backup for VM
```bash
az backup protection enable-for-vm \
  --resource-group myResourceGroup \
  --vault-name myRecoveryVault \
  --vm myVM \
  --policy-name myBackupPolicy
```

### Trigger on-demand backup
```bash
az backup backup-now \
  --resource-group myResourceGroup \
  --vault-name myRecoveryVault \
  --item-name myVM \
  --backup-type Full \
  --retain-until $(date -d "+30 days" +%Y-%m-%d)
```

## Examples
### Restore VM from recovery point
```bash
az backup restore restore-disks \
  --resource-group myResourceGroup \
  --vault-name myRecoveryVault \
  --item-name myVM \
  --rp-name "Backup hourly;2023-01-01T02:00:00+00:00" \
  --storage-account-type Standard_LRS
```

### Check vault backup properties
```bash
az backup vault show \
  --resource-group myResourceGroup \
  --name myRecoveryVault
```

## Related Errors
- {{< relref "/cloud/azure/azure-site-recovery-error" >}}
- {{< relref "/cloud/azure/azure-vm-error" >}}
- {{< relref "/cloud/azure/azure-storage-error" >}}
