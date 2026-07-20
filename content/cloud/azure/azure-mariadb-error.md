---
title: "[Solution] Azure MariaDB Error — connection, performance, and authentication failures"
description: "Fix Azure MariaDB error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 128
---

MariaDB errors appear as connection drops, query timeouts, or authentication failures when accessing single server instances.

## Common Causes
- Server SKU overcommitted with high CPU and memory pressure
- Long-running queries holding table locks blocking new connections
- Firewall rules missing for application server IP ranges
- MariaDB version compatibility issues with newer client libraries
- AAD token expiry causing intermittent authentication failures

## How to Fix
### Check server performance metrics
```bash
az monitor metrics list \
  --resource /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.DBforMariaDB/servers/myMariaServer \
  --metric "cpu_percent,io_requests"
```

### Add firewall rule
```bash
az mariadb server firewall-rule create \
  --resource-group myResourceGroup \
  --server-name myMariaServer \
  --name AllowAppIP \
  --start-ip-address 10.0.0.5 \
  --end-ip-address 10.0.0.5
```

### Update server SKU
```bash
az mariadb server update \
  --resource-group myResourceGroup \
  --name myMariaServer \
  --sku GP_Gen5_4
```

### Enable slow query log
```bash
az mariadb server configuration set \
  --resource-group myResourceGroup \
  --server-name myMariaServer \
  --name slow_query_log \
  --value ON
```

## Examples
### Create MariaDB server
```bash
az mariadb server create \
  --resource-group myResourceGroup \
  --name myMariaServer \
  --admin-user mariadbadmin \
  --admin-password Password123! \
  --sku-name GP_Gen5_2 \
  --storage-size 100
```

### Restore server to point in time
```bash
az mariadb server restore \
  --resource-group myResourceGroup \
  --name myMariaRestored \
  --server-name myMariaServer \
  --restore-point-in-time 2023-01-01T00:00:00
```

## Related Errors
- {{< relref "/cloud/azure/azure-mysql-error" >}}
- {{< relref "/cloud/azure/azure-postgresql-error" >}}
- {{< relref "/cloud/azure/azure-sql-error" >}}
