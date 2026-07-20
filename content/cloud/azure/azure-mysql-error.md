---
title: "[Solution] Azure MySQL Error — connection, SSL, and query failures"
description: "Fix Azure MySQL error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 127
---

MySQL errors manifest as connection refused, SSL handshake failures, or slow queries that exceed timeout limits on flexible or single server deployments.

## Common Causes
- SSL enforcement requiring TLS 1.2 but client only supports older versions
- Azure firewall rules blocking client application connections
- Server resource limits reached with high CPU or IOPS usage
- Flexible server stopped or in paused state requiring resume
- AAD authentication token expired without refresh

## How to Fix
### Check MySQL server state
```bash
az mysql flexible-server show \
  --resource-group myResourceGroup \
  --name myMysqlServer \
  --query "state"
```

### Allow client IP through firewall
```bash
az mysql flexible-server firewall-rule create \
  --resource-group myResourceGroup \
  --name myMysqlServer \
  --rule-name AllowAppServer \
  --start-ip-address 10.0.0.10 \
  --end-ip-address 10.0.0.10
```

### Update SSL settings
```bash
az mysql flexible-server update \
  --resource-group myResourceGroup \
  --name myMysqlServer \
  --ssl-enforcement Enabled \
  --min-tls-version TLS1_2
```

### Restart server to clear connections
```bash
az mysql flexible-server restart \
  --resource-group myResourceGroup \
  --name myMysqlServer
```

## Examples
### Create MySQL flexible server
```bash
az mysql flexible-server create \
  --resource-group myResourceGroup \
  --name myMysqlServer \
  --admin-user mysqladmin \
  --admin-password Password123! \
  --sku-name Standard_D2s_v3 \
  --tier GeneralPurpose \
  --storage-size 128
```

### Export database to blob storage
```bash
az mysql flexible-server export \
  --resource-group myResourceGroup \
  --name myMysqlServer \
  --storage-account myStorageAccount \
  --storage-key myStorageKey \
  --admin-user mysqladmin \
  --admin-password Password123! \
  --database-name mydb
```

## Related Errors
- {{< relref "/cloud/azure/azure-postgresql-error" >}}
- {{< relref "/cloud/azure/azure-sql-error" >}}
- {{< relref "/cloud/azure/azure-mariadb-error" >}}
