---
title: "[Solution] CockroachDB Privilege Error — How to Fix"
description: "Fix CockroachDB insufficient privilege errors by granting correct permissions, managing roles, understanding default access, and implementing least-privilege access."
tools: ["cockroachdb"]
error-types: ["privilege-error"]
severities: ["error"]
weight: 5
comments: true
---

A CockroachDB privilege error occurs when a user or role attempts an operation they are not authorized to perform. CockroachDB uses a role-based access control (RBAC) system that requires explicit grants for most operations.

## Why It Happens

CockroachDB follows the principle of least privilege. By default, new users have no permissions beyond connecting to the database. Privileges must be granted explicitly for each database, table, and operation type.

- The user has not been granted the required privileges on the target object
- The user is a member of a role that does not have the necessary grants
- Public role privileges have been revoked for security hardening
- The user is trying to perform admin-only operations (e.g., CREATE USER, GRANT)
- Schema changes require CREATEROLE or CREATEDB privileges
- The user is accessing a table through a view that has different permissions
- Multi-database setups require grants on each database independently
- The root user has been locked or its password changed without distributing the new credentials

## Common Error Messages

```text
ERROR: permission denied for table users
```

The user does not have SELECT, INSERT, UPDATE, or DELETE on the target table.

```text
ERROR: permission denied for database mydb
```

The user does not have CONNECT or CREATE privileges on the target database.

```text
ERROR: only admin users can use GRANT
```

Only users with the ADMIN option can grant privileges to other users.

```text
ERROR: role "app_user" does not exist
```

The role being referenced has not been created yet.

## How to Fix It

### 1. Grant Table-Level Privileges

```sql
-- Grant SELECT on a specific table
GRANT SELECT ON TABLE users TO app_user;

-- Grant multiple privileges
GRANT SELECT, INSERT, UPDATE ON TABLE orders TO app_user;

-- Grant all privileges on a table
GRANT ALL ON TABLE users TO app_user;

-- Grant privileges on all tables in a schema
GRANT SELECT ON ALL TABLES IN SCHEMA public TO app_user;
```

### 2. Grant Database-Level Privileges

```sql
-- Allow connecting to the database
GRANT CONNECT ON DATABASE mydb TO app_user;

-- Allow creating tables in the database
GRANT CREATE ON DATABASE mydb TO app_user;

-- Allow dropping tables
GRANT DROP ON DATABASE mydb TO app_user;
```

### 3. Create and Manage Roles

```sql
-- Create a new role
CREATE ROLE app_readonly;

-- Grant privileges to the role
GRANT SELECT ON ALL TABLES IN SCHEMA public TO app_readonly;
GRANT CONNECT ON DATABASE mydb TO app_readonly;

-- Create a user and add them to the role
CREATE USER app_user1 WITH PASSWORD 'secure_password';
GRANT app_readonly TO app_user1;

-- Check role membership
SHOW ROLES;

-- Check what privileges a role has
SHOW GRANTS ON DATABASE mydb;
SHOW GRANTS ON TABLE users;

-- Revoke a privilege
REVOKE INSERT ON TABLE users FROM app_user;

-- Remove a user from a role
REVOKE app_readonly FROM app_user1;
```

### 4. Use Admin Role for Schema Changes

```sql
-- Only admin users can perform these operations
-- Check if you are an admin
SHOW is_admin;

-- To make a user an admin (must be done by an existing admin)
CREATE USER admin_user WITH PASSWORD 'admin_password';
GRANT admin TO admin_user;

-- Schema change operations that require admin:
-- CREATE USER, DROP USER, GRANT, REVOKE
-- CREATE DATABASE, DROP DATABASE
-- CREATE ROLE, DROP ROLE
```

### 5. Revoke Public Privileges

```sql
-- By default, the public role has some privileges
-- Revoke them for security
REVOKE ALL ON DATABASE mydb FROM public;
REVOKE ALL ON ALL TABLES IN SCHEMA public FROM public;

-- Now only explicitly granted users can access the database
```

### 6. Audit Current Privileges

```sql
-- Show all grants on all tables in a database
SHOW GRANTS ON TABLE mydb.*;

-- Show grants for a specific user
SHOW GRANTS FOR app_user;

-- Show grants on a specific table
SHOW GRANTS ON TABLE users;

-- Check if a specific user has a specific privilege
-- by examining the grants output
```

## Common Scenarios

**Application user cannot INSERT after schema change.** New tables do not inherit grants from existing tables. Re-run `GRANT` statements for the new table, or use `GRANT ... ON ALL TABLES IN SCHEMA` to grant on all existing tables.

**Read-only user can still see system tables.** System tables in `crdb_internal` and `system` schemas have different access controls. Revoke `SELECT` on `crdb_internal` for untrusted users.

**Root user password lost.** If you have SSH access to a node, you can restart CockroachDB in insecure mode temporarily to reset the root password, then re-enable security.

## Prevent It

- Create roles for common permission sets (readonly, readwrite, admin) and assign users to roles instead of granting individual privileges
- Regularly audit privileges with `SHOW GRANTS` and remove unused or overly broad grants
- Use `GRANT ... ON ALL TABLES IN SCHEMA` to apply consistent permissions across all tables in a schema
