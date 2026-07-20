---
title: "[Solution] Azure SQL Managed Instance Error — networking, backup, and restore failures"
description: "Fix Azure SQL Managed Instance error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 134
---

SQL Managed Instance errors appear as network connectivity failures, backup corruption, or restore operations that fail due to VNet configuration issues.

## Common Causes
- Managed instance VNet subnet delegation not configured properly
- NSG rules blocking management traffic ports 9000/9003
- Backup file corruption or incompatible SQL Server version for restore
- Insufficient vCores for concurrent backup operations
- Route table missing route to managed instance subnet

## How to Fix
### Check managed instance state
```bash
az sql mi show \
  --resource-group myResourceGroup \
  --name myManagedInstance \
  --query "state"
```

### Configure NSG for managed instance
```bash
az network nsg rule create \
  --resource-group myResourceGroup \
  --nsg-name myNSG \
  --name AllowManagementTraffic \
  --priority 100 \
  --destination-port-ranges 9000 9003 \
  --access Allow \
  --protocol Tcp \
  --direction Inbound
```

### List backup status
```bash
az sql mi show-backup-status \
  --resource-group myResourceGroup \
  --name myManagedInstance
```

### Restore database from backup
```bash
az sql db restore \
  --resource-group myResourceGroup \
  --mi myManagedInstance \
  --name myDatabase \
  --dest-name myRestoredDatabase \
  --backup-type "Full" \
  --edition GeneralPurpose
```

## Examples
### Create managed instance
```bash
az sql mi create \
  --resource-group myResourceGroup \
  --name myManagedInstance \
  --admin-user sqladmin \
  --admin-password Password123! \
  --vnet-name myVNet \
  --subnet mySubnet \
  --v-cores 8 \
  --storage-size-in-gb 256 \
  --sku GP_Gen5
```

### List managed instance databases
```bash
az sql db list \
  --resource-group myResourceGroup \
  --mi myManagedInstance \
  --query "[].{name:name,status:status}"
```

## Related Errors
- {{< relref "/cloud/azure/azure-sql-error" >}}
- {{< relref "/cloud/azure/azure-vnet-error" >}}
- {{< relref "/cloud/azure/azure-backup-error" >}}
