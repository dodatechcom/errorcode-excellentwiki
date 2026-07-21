---
title: "[Solution] TiDB Grant Error — How to Fix"
description: "Fix TiDB grant errors by resolving privilege assignment failures, fixing role inheritance issues, and correcting GRANT syntax"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Grant Error

TiDB grant errors occur when attempting to assign or revoke privileges that are invalid, insufficient, or incompatible with the user's role or the target object.

## Why It Happens

- User or role does not exist when GRANT is executed
- Privilege does not exist in TiDB (e.g., TRIGGER on older versions)
- Granting privileges on a non-existent database or table
- Missing WITH GRANT OPTION on the granting user
- Granting a global privilege to a database-level grant
- Revoking a privilege that was never granted

## Common Error Messages

```
ERROR: user 'app_user' does not exist
```

```
ERROR: there is no such grant defined
```

```
ERROR: privilege denied for table 'secret_data'
```

```
ERROR: illegal privilege specified
```

## How to Fix It

### 1. Verify User Exists Before Granting

```sql
-- Check if user exists
SELECT user, host FROM mysql.user
WHERE user = 'app_user';

-- Create user first if needed
CREATE USER 'app_user'@'%' IDENTIFIED BY 'password';

-- Then grant privileges
GRANT SELECT, INSERT ON mydb.* TO 'app_user'@'%';
```

### 2. Fix Invalid Privilege Names

```sql
-- TiDB supports these privileges
SHOW PRIVILEGES;

-- Grant valid privileges only
GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'app_user'@'%';

-- For database-level privileges
GRANT CREATE, ALTER, DROP ON mydb.* TO 'admin'@'%';

-- Global privileges
GRANT PROCESS, REPLICATION SLAVE ON *.* TO 'repl'@'%';
```

### 3. Fix Grant Syntax

```sql
-- Correct syntax for table-level grant
GRANT SELECT ON mydb.users TO 'reader'@'%';

-- Correct syntax for column-level grant
GRANT SELECT (id, name) ON mydb.users TO 'limited'@'%';

-- Correct syntax for procedure grant
GRANT EXECUTE ON PROCEDURE mydb.my_proc TO 'executor'@'%';
```

### 4. Resolve Role-Based Grant Issues

```sql
-- Create role first
CREATE ROLE 'app_read', 'app_write';

-- Grant privileges to roles
GRANT SELECT ON mydb.* TO 'app_read';
GRANT INSERT, UPDATE, DELETE ON mydb.* TO 'app_write';

-- Assign roles to users
GRANT 'app_read', 'app_write' TO 'app_user'@'%';

-- Set default roles
SET DEFAULT ROLE ALL TO 'app_user'@'%';
```

## Common Scenarios

- **User not found during GRANT**: Create the user with proper host specification first.
- **Unknown privilege error**: Use `SHOW PRIVILEGES` to check supported privileges.
- **Grant works but no access**: Ensure the role is activated with `SET ROLE`.

## Prevent It

- Always create users before granting privileges
- Use `SHOW PRIVILEGES` to verify supported privilege names
- Set default roles after granting role memberships

## Related Pages

- [TiDB Auth Error](/tools/tidb/tidb-auth-error)
- [TiDB DDL Error](/tools/tidb/tidb-ddl-error)
- [TiDB Statement Error](/tools/tidb/tidb-statement-error)
