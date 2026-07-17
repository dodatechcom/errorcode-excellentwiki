---
title: "Oracle - ORA-01031: insufficient privileges"
description: "Oracle operation fails because the user does not have the required database privileges"
tools: ["oracle"]
error-types: ["database-error"]
severities: ["error"]
tags: ["oracle", "privileges", "permission", "grants", "ora-01031", "role"]
weight: 5
---

ORA-01031: insufficient privileges occurs when a database user attempts an operation they do not have permission for. This commonly affects DDL operations, PL/SQL compilation, and data access.

## Common Causes

- User lacks CREATE TABLE, CREATE VIEW, or other DDL privileges
- Missing SELECT on system tables or views
- PL/SQL procedure requires grants the user does not have
- Role not granted or not activated
- SYSDBA/SYSOPER privilege required but not granted

## How to Fix

1. Check current user's privileges:

```sql
SELECT * FROM session_privs;
SELECT * FROM session_roles;
```

2. Grant required privileges:

```sql
-- Connect as DBA
GRANT CREATE TABLE TO myuser;
GRANT CREATE VIEW TO myuser;
GRANT CREATE PROCEDURE TO myuser;
GRANT CREATE SEQUENCE TO myuser;
```

3. Grant system privileges via role:

```sql
CREATE ROLE app_developer;
GRANT CREATE TABLE, CREATE VIEW, CREATE PROCEDURE TO app_developer;
GRANT app_developer TO myuser;
```

4. Grant specific object privileges:

```sql
GRANT SELECT, INSERT, UPDATE, DELETE ON schema.table_name TO myuser;
GRANT SELECT ON dba_tab_columns TO myuser;
```

5. For SYSDBA operations:

```sql
-- Connect as SYSDBA
sqlplus / as sysdba
GRANT SYSDBA TO myuser;
```

6. Check granted roles:

```sql
SELECT grantee, granted_role, admin_option
FROM dba_role_privs
WHERE grantee = 'MYUSER';
```

## Examples

```sql
-- Error: ORA-01031: insufficient privileges
CREATE TABLE test (id NUMBER);
-- ORA-01031: insufficient privileges

-- Fix: grant privilege
-- As DBA:
GRANT CREATE TABLE TO myuser;

-- Then retry
CREATE TABLE test (id NUMBER);
-- Table created.
```

## Related Errors

- [Auth error]({{< relref "/tools/oracle/oracle-auth-error" >}})
- [Lock error]({{< relref "/tools/oracle/oracle-lock-error" >}})
