---
title: "[Solution] ClickHouse User Access Error — How to Fix"
description: "Fix ClickHouse user access errors including authentication failures, permission denied issues, and user management problems"
tools: ["clickhouse"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ClickHouse User Access Error

User access errors in ClickHouse occur when authentication fails, users lack required permissions, or user configuration is incorrect. ClickHouse has its own user management system separate from OS users.

## Why It Happens

- The username or password is incorrect
- The user account does not exist in ClickHouse
- The user lacks permissions for the requested operation
- The user is connecting from an unauthorized IP address
- The `<allow_remote_hosts>` setting blocks the connection
- The user profile has restrictive quotas

## Common Error Messages

```
Code: 192. DB::Exception: Name 'myuser' is not found in Users directory
```

```
Code: 210. DB::Exception: Connection refused
```

```
Code: 497. DB::Exception: myuser: Authentication failed
```

```
Code: 194. DB::Exception: User 'myuser' is not allowed to connect from host '192.168.1.100'
```

## How to Fix It

### 1. Create or Fix User

```sql
-- Create a new user
CREATE USER IF NOT EXISTS 'myuser'@'192.168.1.%' IDENTIFIED WITH sha256_password BY 'password';

-- Grant permissions
GRANT SELECT, INSERT ON mydb.* TO 'myuser'@'192.168.1.%';

-- Check existing users
SELECT name, auth_type, host_ip_restrictions FROM system.users;
```

### 2. Fix Authentication Issues

```xml
<!-- In /etc/clickhouse-server/users.d/myuser.xml -->
<clickhouse>
  <users>
    <myuser>
      <password>password</password>
      <networks>
        <ip>192.168.1.0/24</ip>
        <ip>127.0.0.1</ip>
      </networks>
      <profile>default</profile>
      <quota>default</quota>
    </myuser>
  </users>
</clickhouse>
```

### 3. Fix Permission Denied Errors

```sql
-- Check user permissions
SHOW GRANTS FOR 'myuser'@'192.168.1.%';

-- Grant additional permissions
GRANT ALL ON mydb.* TO 'myuser'@'192.168.1.%';

-- Or grant specific permissions
GRANT SELECT ON system.* TO 'myuser'@'192.168.1.%';
```

### 4. Fix IP Restrictions

```sql
-- Check network restrictions
SELECT name, host_ip_restrictions FROM system.users;

-- Update network restrictions
ALTER USER 'myuser'@'192.168.1.%' HOST IP '192.168.1.0/24' IDENTIFIED BY 'password';
```

## Common Scenarios

- **New application cannot connect**: User does not exist. Create user with correct IP restrictions.
- **Permission denied on system tables**: Grant SELECT on system.* to the user.
- **Authentication fails after password change**: Update password in users.d/*.xml and restart.

## Prevent It

- Use IP restrictions instead of allowing connections from anywhere
- Store passwords securely, not in plaintext config files
- Create dedicated users with minimal required permissions

## Related Pages

- [ClickHouse Connection Error](/tools/clickhouse/clickhouse-connection-error)
- [ClickHouse HTTP Error](/tools/clickhouse/clickhouse-http-error)
- [ClickHouse Quota Error](/tools/clickhouse/clickhouse-quota-error)
