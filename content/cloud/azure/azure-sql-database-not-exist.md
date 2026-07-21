---
title: "[Solution] AZURE SQL Database Not Found"
description: "ResourceNotFound when the specified database does not exist."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `SQL Database Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Database name is incorrect
- Database was deleted
- Database on different server
- Database in elastic pool

## How to Fix

### Check database

```bash
az sql db show --name mydb --server myserver --resource-group myRG
```
### List databases

```bash
az sql db list --server myserver --resource-group myRG --query "[].{Name:name,Status:status}" --output table
```
### Create database

```bash
az sql db create --name mydb --server myserver --resource-group myRG --service-tier Basic
```

## Examples

- Database mydb not found on server myserver
- Database deleted and needs restore

## Related Errors

- [Azure SQL Error]({{< relref "/cloud/azure/azure-sql-error" >}}) -- General SQL errors
- [Connection Failed]({{< relref "/cloud/azure/azure-sql-connection-failed" >}}) -- Connection
