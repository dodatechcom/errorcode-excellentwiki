---
title: "[Solution] TiDB Auth Error — How to Fix"
description: "Fix TiDB authentication errors by configuring user accounts, resolving password issues, and fixing role-based access control"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Auth Error

TiDB authentication errors occur when users fail to authenticate or lack required privileges. TiDB supports MySQL-compatible authentication.

## Why It Happens

- Username or password is incorrect
- User does not exist in the database
- User lacks required privileges
- SSL certificate authentication fails
- Authentication plugin is not supported
- Password has expired

## Common Error Messages

```
ERROR: Access denied for user
```

```
ERROR: user does not exist
```

```
ERROR: privileges not sufficient
```

```
ERROR: authentication plugin not supported
```

## How to Fix It

### 1. Create User

```sql
-- Create user with password
CREATE USER 'app_user'@'%' IDENTIFIED BY 'secure_password';

-- Create user with specific host
CREATE USER 'app_user'@'10.0.0.%' IDENTIFIED BY 'secure_password';

-- Create read-only user
CREATE USER 'readonly'@'%' IDENTIFIED BY 'readonly_password';
GRANT SELECT ON mydb.* TO 'readonly'@'%';
```

### 2. Fix Password Issues

```sql
-- Reset password
ALTER USER 'app_user'@'%' IDENTIFIED BY 'new_password';

-- Check user exists
SELECT user, host FROM mysql.user WHERE user = 'app_user';

-- Grant privileges
GRANT ALL PRIVILEGES ON mydb.* TO 'app_user'@'%';
FLUSH PRIVILEGES;
```

### 3. Configure SSL Authentication

```sql
-- Create user requiring SSL
CREATE USER 'secure_user'@'%' IDENTIFIED BY 'password' REQUIRE SSL;

-- Check user SSL settings
SELECT user, host, ssl_type FROM mysql.user;
```

### 4. Check Privileges

```sql
-- Check user privileges
SHOW GRANTS FOR 'app_user'@'%';

-- Grant specific privileges
GRANT SELECT, INSERT, UPDATE ON mydb.users TO 'app_user'@'%';

-- Revoke privileges
REVOKE DELETE ON mydb.* FROM 'app_user'@'%';
```

## Common Scenarios

- **New deployment allows any access**: Configure authentication before exposing to network.
- **Application cannot authenticate**: Ensure user exists and password matches.
- **User cannot access table**: Grant appropriate privileges.

## Prevent It

- Use strong passwords and least-privilege principles
- Configure authentication before exposing cluster
- Monitor failed authentication attempts

## Related Pages

- [TiDB Connection Error](/tools/tidb/tidb-connection-error)
- [TiDB Config Error](/tools/tidb/tidb-gflag-error)
- [TiDB SSL Error](/tools/tidb/tidb-auth-error)
