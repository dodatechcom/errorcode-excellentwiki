---
title: "[Solution] Linux PostgreSQL Role Not Found Error"
description: "Fix Linux PostgreSQL 'role not found' errors. Create missing roles, fix authentication, and resolve role configuration issues."
platforms: ["linux"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: PostgreSQL — role not found

The `FATAL: role "<role>" does not exist` or `FATAL: role "postgres" does not exist` error means the PostgreSQL server does not have a database role (user) with the specified name. Roles in PostgreSQL encompass users, groups, and system privileges. This error occurs during connection when the client specifies a username that has not been created on the server.

## What This Error Means

PostgreSQL uses roles for authentication and authorization. Every connection must specify a role name. When the server receives a connection request with a role name that does not exist in `pg_roles`, it immediately rejects the connection. This is different from `password authentication failed` — that error means the role exists but the password is wrong.

## Common Causes

- Role was never created on the target server
- Connecting to the wrong database or server
- Role was dropped or renamed
- Restoring a database dump without the roles
- Misspelled role name or case sensitivity issue
- Different PostgreSQL installations with different roles

## How to Fix

### 1. Check Existing Roles

```bash
# Connect as superuser (usually postgres)
sudo -u postgres psql

# List all roles
\du

# Or query directly
SELECT rolname FROM pg_roles;
```

### 2. Create the Missing Role

```sql
-- Create a role (user)
CREATE ROLE myuser WITH LOGIN PASSWORD 'secure_password';

-- Or with more privileges
CREATE ROLE myuser WITH LOGIN SUPERUSER PASSWORD 'secure_password';

-- Create with specific options
CREATE ROLE myuser
  WITH LOGIN
  CREATEDB
  CREATEROLE
  CONNECTION LIMIT 10
  PASSWORD 'secure_password';
```

### 3. Fix Common Authentication Issues

```sql
-- If connecting as 'postgres' user fails
-- Check pg_hba.conf for local connections
-- The postgres role should always exist

-- If 'postgres' role is missing (very rare)
-- You may need to recreate the cluster
sudo pg_dropcluster 15 main
sudo pg_createcluster 15 main
```

### 4. Restore Roles from Dump

```bash
# When restoring from pg_dumpall, restore roles first
sudo -u postgres psql -f /path/to/roles.sql

# Or extract roles from dump
pg_restore -l backup.dump | grep ROLE > roles.list
pg_restore -L roles.list -d mydb backup.dump

# Or manually create roles from the dump
grep 'CREATE ROLE' backup.sql
```

### 5. Fix Role Name Case Sensitivity

```sql
-- PostgreSQL folds unquoted names to lowercase
-- This fails if role was created with quotes
CREATE ROLE "MyUser" WITH LOGIN PASSWORD 'pass';  -- Creates "MyUser" (case-sensitive)

-- Connection must use the exact case:
psql -U MyUser    -- fails (looks for "myuser")
psql -U "MyUser"  -- works

-- Best practice: use lowercase names
CREATE ROLE myuser WITH LOGIN PASSWORD 'pass';
```

### 6. Grant Role to Another Role

```sql
-- Add a role to a group role
GRANT group_role TO user_role;

-- Check role membership
SELECT rolname, rolsuper, rolcreaterole, rolcreatedb
FROM pg_roles
WHERE rolname = 'myuser';
```

### 7. Fix pg_hba.conf for the Role

```bash
# Ensure pg_hba.conf allows the role to connect
sudo nano /etc/postgresql/15/main/pg_hba.conf

# Add entry for the specific role:
# local   all   myuser   scram-sha-256

# Or allow all users:
# local   all   all      scram-sha-256

sudo systemctl restart postgresql
```

## Examples

```bash
$ psql -h localhost -U myuser -d mydb
psql: error: connection to server at "localhost" (127.0.0.1), port 5432 failed:
FATAL:  role "myuser" does not exist

$ sudo -u postgres psql -c "\du"
                             List of roles
 Role name |                         Attributes
-----------+-----------------------------------------------------
 postgres  | Superuser, Create role, Create DB, Replication

$ sudo -u postgres psql -c "CREATE ROLE myuser WITH LOGIN PASSWORD 'mypass';"
CREATE ROLE

$ psql -h localhost -U myuser -d mydb
mydb=>
```

## Related Errors

- [PostgreSQL connection refused]({{< relref "/os/linux/linux-postgres-connection-refused" >}}) — Server not accepting connections
- [MySQL connection refused]({{< relref "/os/linux/linux-mysql-connection-refused" >}}) — MySQL connection issues
- [Permission denied]({{< relref "/os/linux/permission-denied10" >}}) — General permission issues
