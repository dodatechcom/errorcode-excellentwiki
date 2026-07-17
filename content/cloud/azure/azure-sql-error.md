---
title: "[Solution] Azure SQL Connection Error"
description: "Fix Azure SQL connection errors. Resolve Azure SQL Database connectivity issues."
cloud: ["azure"]
error-types: ["api-error"]
severities: ["error"]
tags: ["azure", "sql", "database", "connection", "firewall"]
weight: 5
---

An Azure SQL connection error occurs when you cannot connect to Azure SQL Database. This can be caused by firewall rules, authentication, or configuration issues.

## Common Causes

- Client IP not in SQL Server firewall rules
- Incorrect connection string (server, database, credentials)
- Azure AD authentication not configured
- SQL Server is paused (serverless tier)
- Network security group blocking traffic

## How to Fix

### Check SQL Server Status

```bash
az sql server show --name myserver --resource-group myRG --query 'state'
```

### Add Firewall Rule

```bash
az sql server firewall-rule create --resource-group myRG --server myserver \
  --name AllowMyIP --start-ip-address 1.2.3.4 --end-ip-address 1.2.3.4
```

### Allow Azure Services

```bash
az sql server firewall-rule create --resource-group myRG --server myserver \
  --name AllowAzure --start-ip-address 0.0.0.0 --end-ip-address 0.0.0.0
```

### Test Connection

```bash
sqlcmd -S myserver.database.windows.net -d mydb -U myuser -P mypassword
```

### Check Connection String

```bash
az webapp config connection-string list --name myapp --resource-group myRG
```

## Examples

```bash
# Example 1: Firewall blocked
# Client IP 1.2.3.4 is not allowed to access the server
# Fix: add firewall rule for client IP

# Example 2: Server paused
# Database is paused due to inactivity
# Fix: resume the serverless database
```

## Related Errors

- [Azure Cosmos Error]({{< relref "/cloud/azure/azure-cosmos-error" >}}) — Cosmos DB error
- [Azure AD Error]({{< relref "/cloud/azure/azure-ad-error" >}}) — AD authentication error
