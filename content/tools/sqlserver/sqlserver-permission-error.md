---
title: "SQL Server Permission Denied Error"
description: "SQL Server operation fails due to insufficient permissions."
tools: ["sqlserver"]
error-types: ["database-error"]
severities: ["error"]
tags: ["sqlserver", "permission", "grant", "role", "access"]
weight: 5
---

# SQL Server Permission Denied Error

A SQL Server permission denied error occurs when a user lacks the necessary database permissions to perform an operation.

## Common Causes

- Missing SELECT, INSERT, UPDATE, or DELETE permissions
- User not mapped to database
- Database role not assigned
- Object-level permissions not granted

## How to Fix

### Check User Permissions

```sql
SELECT dp.name, dp.type_desc
FROM sys.database_principals dp
JOIN sys.database_role_members drm ON dp.principal_id = drm.member_principal_id;
```

### Grant Database Role

```sql
ALTER ROLE db_datareader ADD MEMBER myuser;
ALTER ROLE db_datawriter ADD MEMBER myuser;
```

### Grant Object Permissions

```sql
GRANT SELECT, INSERT, UPDATE, DELETE ON dbo.users TO myuser;
```

### Check Server-Level Permissions

```sql
SELECT sp.name, sp.type_desc, sl.permission_name
FROM sys.server_principals sp
JOIN sys.server_permissions sl ON sp.principal_id = sl.grantee_principal_id;
```

### Grant Server Permissions

```sql
GRANT VIEW SERVER STATE TO myuser;
```

### Create User with Login

```sql
CREATE LOGIN myuser WITH PASSWORD = 'password';
USE mydb;
CREATE USER myuser FOR LOGIN myuser;
ALTER ROLE db_datareader ADD MEMBER myuser;
```

## Examples

```sql
SELECT * FROM dbo.users;
-- The SELECT permission was denied on the object 'users', database 'mydb', schema 'dbo'.
```

## Related Errors

- [Auth Error]({{< relref "/tools/sqlserver/error-18456" >}}) — login failed
- [Deadlock Error]({{< relref "/tools/sqlserver/sqlserver-deadlock-error" >}}) — deadlock detected
