---
title: "[Solution] PostgreSQL Role Does Not Exist - Fix Missing User Errors"
description: "Fix PostgreSQL role does not exist errors by creating the missing role, correcting the username, and verifying search_path settings"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Role Does Not Exist

This error occurs when a SQL statement references a role (user or group) that has not been created in the PostgreSQL cluster. In PostgreSQL, users and roles are the same object -- there is no separate USER type.

## What This Error Means

PostgreSQL returns this error when it cannot find the specified role in the `pg_roles` system catalog:

```
ERROR: role "myuser" does not exist
```

This can appear during `GRANT` statements, `ALTER DEFAULT PRIVILEGES`, connection attempts, or when a query references a role in a `SET ROLE` command. The role may have been dropped, never created, or the name may be misspelled.

PostgreSQL roles are cluster-wide, not database-specific. If a role exists in one database, it exists in all databases on the same cluster. The error means the role does not exist at the cluster level.

## Why It Happens

- The role was never created after a fresh PostgreSQL installation or migration
- A migration script drops and recreates roles in the wrong order
- The role name is case-sensitive and was created with quotes but referenced without them
- `search_path` includes a schema that contains objects owned by a now-deleted role
- Connecting to a different PostgreSQL cluster than expected
- Copying SQL dumps that reference roles not yet restored

## How to Fix It

### 1. Check If the Role Exists

```sql
SELECT rolname FROM pg_roles WHERE rolname = 'myuser';
```

### 2. Create the Missing Role

```sql
-- Create a login role
CREATE ROLE myuser WITH LOGIN PASSWORD 'secure_password';

-- Create a role with more privileges
CREATE ROLE myuser WITH LOGIN CREATEDB CREATEROLE PASSWORD 'secure_password';
```

### 3. Fix Case Sensitivity

```sql
-- Roles created with quotes preserve case
CREATE ROLE "MyUser" WITH LOGIN PASSWORD 'pass';

-- Without quotes, PostgreSQL lowercases the name
CREATE ROLE MyUser WITH LOGIN PASSWORD 'pass';
-- This creates "myuser", not "MyUser"

-- To find the exact name
SELECT rolname FROM pg_roles WHERE rolname ILIKE '%myuser%';
```

### 4. Grant Ownership After Role Creation

```sql
-- Transfer table ownership to the new role
ALTER TABLE mytable OWNER TO myuser;

-- Transfer all tables in a schema
ALTER OWNERSHIP ON ALL TABLES IN SCHEMA public TO myuser;
```

### 5. Restore from a Role Dump

```bash
# If you have a roles dump
pg_restore -d postgres --data-only --roles-only roles.dump

# Or create roles manually from a SQL dump
grep "CREATE ROLE" roles.sql | psql -d postgres
```

## Common Mistakes

- Creating the role in one database and assuming it is database-specific -- roles are cluster-wide
- Forgetting that `CREATE USER` is an alias for `CREATE ROLE WITH LOGIN`
- Using uppercase role names without quoting and getting unexpected mismatches
- Not restoring roles before restoring database objects that depend on them
- Running migrations that assume roles exist without checking first

## Related Pages

- [PostgreSQL Permission Denied](/tools/postgresql/pg-permission-denied)
- [PostgreSQL Connection Refused](/tools/postgresql/pg-connection-refused)
- [PostgreSQL Database Does Not Exist](/tools/postgresql/pg-database-does-not-exist)
- [MySQL Access Denied](/tools/mysql/mysql-access-denied)
