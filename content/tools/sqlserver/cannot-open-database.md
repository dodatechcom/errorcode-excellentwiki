---
title: "Cannot open database 'X' requested by the login"
description: "The login succeeded but SQL Server cannot access the requested database."
tools: ["sqlserver"]
error-types: ["database-error"]
severities: ["error"]
tags: ["database", "permissions", "access", "login"]
weight: 5
---

The `Cannot open database 'X' requested by the login` error means the login authenticated successfully but the user does not have access to the specified database, or the database is offline. The default database assigned to the login may be unavailable.

## Common Causes

- The login's default database is offline or has been dropped
- The user has not been granted `CONNECT` permission on the target database
- The database is in `RESTORING`, `OFFLINE`, or `EMERGENCY` state
- The database was recently restored or attached and permissions were not migrated

## How to Fix

Grant the user access to the database:

```sql
USE target_database;
CREATE USER app_user FOR LOGIN app_user;
GRANT CONNECT TO app_user;
```

Change the login's default database to one that is available:

```sql
ALTER LOGIN app_user WITH DEFAULT_DATABASE = master;
```

Bring an offline database back online:

```sql
ALTER DATABASE target_database SET ONLINE;
```

## Examples

```sql
-- User tries to connect but their default database is offline
sqlcmd -S server_name -U app_user -P password123 -D myapp_db
-- Cannot open database 'myapp_db' requested by the login. Failed to open the database.

-- Check database state
SELECT name, state_desc FROM sys.databases WHERE name = 'myapp_db';
-- Output: myapp_db | OFFLINE
```

Reset the default database so the login can connect, then restore access:

```sql
ALTER LOGIN app_user WITH DEFAULT_DATABASE = master;
-- Now connect and fix permissions
USE myapp_db;
CREATE USER app_user FOR LOGIN app_user;
```

## Related Errors

- [Login failed for user 'X']({{< relref "/tools/sqlserver/login-failed" >}})
