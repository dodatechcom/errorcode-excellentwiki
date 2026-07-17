---
title: "SQL Server Authentication Error"
description: "SQL Server login fails with authentication error."
tools: ["sqlserver"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# SQL Server Authentication Error

A SQL Server authentication error occurs when the client cannot authenticate with the database server. This can be caused by incorrect credentials, disabled authentication mode, or locked accounts.

## Common Causes

- Incorrect username or password
- SQL Server in Windows Authentication mode only
- Account locked or disabled
- Password policy violation

## How to Fix

### Check Authentication Mode

```sql
SELECT SERVERPROPERTY('IsIntegratedSecurityOnly');
-- 1 = Windows only, 0 = Mixed mode
```

### Enable Mixed Mode Authentication

In **SQL Server Management Studio** > **Server Properties** > **Security** > Select **SQL Server and Windows Authentication mode**.

### Create SQL Login

```sql
CREATE LOGIN myuser WITH PASSWORD = 'StrongP@ssw0rd';
CREATE USER myuser FOR LOGIN myuser;
```

### Reset Password

```sql
ALTER LOGIN sa WITH PASSWORD = 'NewP@ssw0rd';
```

### Check Account Status

```sql
SELECT name, is_disabled FROM sys.sql_logins;
```

### Enable Account

```sql
ALTER LOGIN myuser ENABLE;
```

### Fix Connection String

```
Server=myserver;Database=mydb;User Id=myuser;Password=mypassword;
```

## Examples

```sql
sqlcmd -S myserver -U sa -P wrongpassword
Login failed for user 'sa'. (Microsoft SQL Server, Error: 18456)
```

## Related Errors

- [Connection Error]({{< relref "/tools/sqlserver/sqlserver-connection-error" >}}) — connection failure
- [Permission Error]({{< relref "/tools/sqlserver/sqlserver-permission-error" >}}) — permission denied
