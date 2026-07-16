---
title: "[Solution] SQL Server Error 4060: Cannot Open Database"
description: "Fix SQL Server Error 4060 cannot open database errors. Resolve database access and default database issues."
tools: ["sqlserver"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["sqlserver", "4060", "database", "open", "default", "access"]
weight: 5
---

# Error 4060: Cannot Open Database

Error 4060 occurs when SQL Server cannot open the database requested by the login. The user's default database may not exist, or the user may lack CONNECT permission to it.

## Common Causes

- The login's default database has been dropped or is offline
- The user does not have CONNECT permission on the requested database
- The database is in RESTORING or RECOVERY state
- The database files are missing or corrupted

## How to Fix

### Connect to a Different Default Database

```bash
sqlcmd -S server -d master -U sa -P password
```

### Change the Login's Default Database

```sql
ALTER LOGIN app_user WITH DEFAULT_DATABASE = master;
```

### Grant CONNECT Permission

```sql
USE master;
GRANT CONNECT SQL TO app_user;

-- Or grant database access
USE target_database;
CREATE USER app_user FOR LOGIN app_user;
ALTER ROLE db_datareader ADD MEMBER app_user;
```

### Bring Database Online

```sql
ALTER DATABASE mydb SET ONLINE;
```

### Check Database State

```sql
SELECT name, state_desc, is_read_only
FROM sys.databases
WHERE name = 'mydb';
```

## Examples

```bash
# Default database was dropped
sqlcmd -S server -U app_user -P pass
-- Error 4060: Cannot open database "old_db" requested by the login
# Fix: ALTER LOGIN app_user WITH DEFAULT_DATABASE = master

# Database in restoring state
sqlcmd -S server -d mydb -U sa -P pass
-- Error 4060: Cannot open database "mydb"
# Fix: RESTORE DATABASE mydb WITH RECOVERY
```

## Related Errors

- [Error 18456]({{< relref "/tools/sqlserver/error-18456" >}}) — login failed
- [Error 547]({{< relref "/tools/sqlserver/error-547" >}}) — CHECK constraint failed
