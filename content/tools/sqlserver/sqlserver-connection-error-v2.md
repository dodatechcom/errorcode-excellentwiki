---
title: "SQL Server - TCP Provider connection refused"
description: "SQL Server client fails to connect because the TCP provider cannot establish a connection to the server"
tools: ["sqlserver"]
error-types: ["database-error"]
severities: ["error"]
tags: ["sqlserver", "tcp", "connection", "network", "port", "firewall"]
weight: 5
---

A TCP Provider connection refused error occurs when the SQL Server client cannot establish a TCP connection to the database server. This is similar to a general connection error but specifically identifies the TCP transport layer as the point of failure.

## Common Causes

- SQL Server service not running or stopped
- TCP/IP protocol not enabled in SQL Server Configuration Manager
- Incorrect server name or instance in connection string
- Firewall blocking port 1433
- Named instance using dynamic ports not properly configured

## How to Fix

1. Verify SQL Server service is running:

```bash
systemctl status mssql-server  # Linux
Get-Service MSSQLSERVER        # Windows PowerShell
```

2. Check TCP/IP protocol status:

```sql
-- Enable TCP/IP
USE master;
EXEC sp_configure 'remote admin connections', 1;
RECONFIGURE;
```

3. Verify port is listening:

```bash
ss -tlnp | grep 1433
netstat -an | grep 1433
```

4. Fix connection string for different scenarios:

```
-- Default instance
Server=myserver;Database=mydb;Trusted_Connection=yes;

-- Named instance
Server=myserver\instance;Database=mydb;Trusted_Connection=yes;

-- Custom port
Server=myserver,1433;Database=mydb;Trusted_Connection=yes;
```

5. Enable SQL Server Browser for named instances:

```bash
sudo systemctl enable mssql-server
sudo systemctl start sqlservr-browser  # Linux
```

6. Test connectivity with sqlcmd:

```bash
sqlcmd -S myserver -U sa -P password -Q "SELECT @@VERSION"
```

## Examples

```bash
$ sqlcmd -S myserver -U sa -P password
Sqlcmd: Error: Microsoft ODBC Driver 17 for SQL Server : TCP Provider:
No connection could be made because the target machine actively refused it.

# Fix: check if SQL Server is listening
$ ss -tlnp | grep 1433
LISTEN 0 128 0.0.0.0:1433 0.0.0.0:*
```

## Related Errors

- [Auth error]({{< relref "/tools/sqlserver/sqlserver-auth-error" >}})
- [Deadlock error]({{< relref "/tools/sqlserver/sqlserver-deadlock-error" >}})
