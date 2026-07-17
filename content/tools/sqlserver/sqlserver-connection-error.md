---
title: "SQL Server Connection Error"
description: "SQL Server client cannot establish a connection to the database."
tools: ["sqlserver"]
error-types: ["database-error"]
severities: ["error"]
tags: ["sqlserver", "connection", "network", "tcp", "instance"]
weight: 5
---

# SQL Server Connection Error

A SQL Server connection error occurs when the client cannot connect to the SQL Server instance. This is typically caused by network issues, SQL Server configuration, or firewall restrictions.

## Common Causes

- SQL Server service not running
- TCP/IP protocol not enabled
- Incorrect server name or instance
- Firewall blocking port 1433
- Named instance dynamic port issues

## How to Fix

### Check SQL Server Service

```bash
systemctl status mssql-server  # Linux
```

### Verify SQL Server Configuration

```sql
SELECT @@SERVERNAME, @@VERSION;
```

### Enable TCP/IP Protocol

Open **SQL Server Configuration Manager** > **SQL Server Network Configuration** > **Protocols for MSSQLSERVER** > Enable **TCP/IP**.

### Check Port

```bash
ss -tlnp | grep 1433
```

### Fix Connection String

```
# Default instance
Server=myserver;Database=mydb;Trusted_Connection=yes;

# Named instance
Server=myserver\instance;Database=mydb;Trusted_Connection=yes;

# Custom port
Server=myserver,1433;Database=mydb;Trusted_Connection=yes;
```

### Check Firewall

```bash
sudo ufw allow 1433/tcp
```

### Test Connectivity

```bash
sqlcmd -S myserver -U sa -P password -Q "SELECT 1"
```

## Examples

```bash
sqlcmd -S myserver -U sa -P password
Sqlcmd: Error: Microsoft ODBC Driver 17 for SQL Server : TCP Provider: No connection could be made because the target machine actively refused it.
```

## Related Errors

- [Auth Error]({{< relref "/tools/sqlserver/error-18456" >}}) — login failed
- [Cannot Open Database]({{< relref "/tools/sqlserver/cannot-open-database" >}}) — database access error
