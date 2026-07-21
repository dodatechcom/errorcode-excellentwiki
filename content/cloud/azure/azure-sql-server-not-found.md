---
title: "[Solution] AZURE SQL Server Not Found"
description: "ResourceNotFound when the specified SQL server does not exist."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `SQL Server Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Server name is incorrect
- Server was deleted
- Server in different resource group
- Logical server name is case-sensitive

## How to Fix

### Check server

```bash
az sql server show --name myserver --resource-group myRG
```
### List servers

```bash
az sql server list --resource-group myRG --query "[].{Name:name,AdminUser:administratorLogin}" --output table
```
### Create server

```bash
az sql server create --name myserver --resource-group myRG --location eastus --admin-user sqladmin --admin-password MyPassword123!
```

## Examples

- Server myserver not found (check name)
- Server deleted from resource group

## Related Errors

- [Azure SQL Error]({{< relref "/cloud/azure/azure-sql-error" >}}) -- General SQL errors
- [Database Not Found]({{< relref "/cloud/azure/azure-sql-database-not-exist" >}}) -- Database not found
