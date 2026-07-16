---
title: "Login failed for user 'X'"
description: "SQL Server rejected the login attempt due to invalid credentials or authentication misconfiguration."
tools: ["sqlserver"]
error-types: ["database-error"]
severities: ["error"]
tags: ["database", "authentication", "login", "security"]
weight: 5
---

The `Login failed for user 'X'` error occurs when SQL Server cannot authenticate the specified login. This can happen with both SQL Server authentication and Windows authentication depending on the configuration.

## Common Causes

- The username or password is incorrect
- The SQL Server login does not exist in the instance
- Windows Authentication mode is enabled but SQL login credentials were provided (or vice versa)
- The user does not have permission to connect to the server

## How to Fix

Verify the login exists and is enabled:

```sql
SELECT name, is_disabled FROM sys.server_principals WHERE name = 'your_user';
```

Create the login if it does not exist:

```sql
CREATE LOGIN your_user WITH PASSWORD = 'StrongP@ssw0rd';
```

Enable a disabled login:

```sql
ALTER LOGIN your_user ENABLE;
```

Check the server authentication mode:

```sql
SELECT SERVERPROPERTY('IsIntegratedSecurityOnly');
-- Returns 1 for Windows only, 0 for Mixed Mode
```

## Examples

```sql
-- SQL auth attempted on a Windows-only server
sqlcmd -S server_name -U app_user -P password123
-- Msg 18456, Login failed for user 'app_user'

-- Wrong password with correct username
sqlcmd -S server_name -U app_user -P wrongpassword
-- Msg 18456, Login failed for user 'app_user'
```

Enable Mixed Mode authentication in SQL Server Management Studio under **Server Properties > Security** if both auth modes are needed.

## Related Errors

- [Cannot open database 'X']({{< relref "/tools/sqlserver/cannot-open-database" >}})
