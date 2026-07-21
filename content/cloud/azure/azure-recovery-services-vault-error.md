---
title: "[Solution] Azure Recovery Services Vault Error"
description: "Fix Azure Recovery Services vault configuration errors blocking backup and DR operations."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Recovery Services vault errors prevent backup and disaster recovery operations from completing. This affects backup policies, restores, and cross-region recovery.

## Common Causes

- Vault has no backup policies configured
- Vault is in a soft-deleted state and cannot accept new operations
- Cross-region restore is enabled but the secondary region is unavailable
- Storage redundancy configuration conflicts with backup requirements

## How to Fix

### Check vault status

```bash
az backup vault show \
  --name myVault \
  --resource-group myRG \
  --query "properties.provisioningState"
```

### List vault backup policies

```bash
az backup policy list \
  --resource-group myRG \
  --vault-name myVault \
  --query "[].{Name:name,Type:type}"
```

### Create a backup policy

```bash
az backup policy create \
  --resource-group myRG \
  --vault-name myVault \
  --name dailyPolicy \
  --policy '{
    "backupManagementType": "AzureIaasVM",
    "schedulePolicy": {
      "schedulePolicyType": "SimpleSchedulePolicy",
      "scheduleRunFrequency": "Daily",
      "scheduleRunTimes": ["2026-01-01T02:00:00Z"]
    },
    "retentionPolicy": {
      "retentionPolicyType": "LongTermRetentionPolicy",
      "dailySchedule": {
        "retentionTimes": ["2026-01-01T02:00:00Z"],
        "retentionDuration": {"count": 30, "durationType": "Days"}
      }
    }
  }'
```

### Recover a soft-deleted vault

```bash
az backup vault restore \
  --name myVault \
  --resource-group myRG
```

## Examples

- Vault is in soft-deleted state and cannot create new backup policies
- Backup job fails because no policy is assigned to the protected item
- Cross-region restore fails because the secondary region storage account is not accessible

## Related Errors

- [Azure Backup Error]({{< relref "/cloud/azure/azure-backup-error" >}}) -- General backup errors.
- [Azure Backup Inconsistent Error]({{< relref "/cloud/azure/azure-backup-inconsistent-error" >}}) -- Inconsistent backups.
