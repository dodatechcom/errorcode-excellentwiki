---
title: "SQL Server - login failed for user"
description: "SQL Server rejects login attempt because the specified user credentials are invalid or the user does not exist"
tools: ["sqlserver"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

SQL Server "login failed for user" error occurs when the server rejects a login attempt due to incorrect credentials, disabled account, or missing database access permissions. This is the SQL Server equivalent of authentication failure.

## Common Causes

- Incorrect username or password
- SQL Server authentication not enabled (Windows only)
- Login exists but has no access to the target database
- Account locked or disabled
- Password policy violation

## How to Fix

1. Enable mixed mode authentication:

```sql
-- Enable SQL Server and Windows Authentication
EXEC xp_instance_regwrite
  N'HKEY_LOCAL_MACHINE',
  N'Software\Microsoft\MSSQLServer\MSSQLServer',
  N'LoginMode', REG_DWORD, 2;
```

2. Create a SQL login:

```sql
CREATE LOGIN myuser WITH PASSWORD = 'StrongP@ssw0rd!';
USE mydb;
CREATE USER myuser FOR LOGIN myuser;
GRANT SELECT, INSERT, UPDATE, DELETE TO myuser;
```

3. Reset password:

```sql
ALTER LOGIN myuser WITH PASSWORD = 'NewP@ssw0rd!';
```

4. Check login status:

```sql
SELECT name, is_disabled, create_date, modify_date
FROM sys.sql_logins
WHERE name = 'myuser';
```

5. Enable the login:

```sql
ALTER LOGIN myuser ENABLE;
```

6. Test connection:

```bash
sqlcmd -S myserver -U myuser -P StrongP@ssw0rd! -Q "SELECT 1"
```

## Examples

```bash
$ sqlcmd -S myserver -U myuser -P wrongpass
Msg 18456, Level 14, State 1, Server myserver, Line 1
Login failed for user 'myuser'.

# Fix: reset password
$ sqlcmd -S myserver -U sa -P sapassword
> ALTER LOGIN myuser WITH PASSWORD = 'correctpass';
```

## Related Errors

- [Connection error]({{< relref "/tools/sqlserver/sqlserver-connection-error" >}})
- [Permission error]({{< relref "/tools/sqlserver/sqlserver-permission-error" >}})
