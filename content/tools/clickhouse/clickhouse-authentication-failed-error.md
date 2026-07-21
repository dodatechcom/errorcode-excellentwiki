---
title: "[Solution] ClickHouse Authentication Failed Error"
description: "Fix ClickHouse authentication errors when login credentials are rejected"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Authentication Failed Error

Authentication failed errors occur when ClickHouse rejects login credentials.

## Common Causes

- Wrong username or password
- User not created in ClickHouse
- Auth method mismatch (password vs SHA256)
- User account locked or disabled

## How to Fix

Check existing users:

```sql
SELECT name FROM system.users;
```

Create user:

```sql
CREATE USER app_user IDENTIFIED WITH sha256_password BY 'secure_password';
GRANT SELECT, INSERT, UPDATE ON mydb.* TO app_user;
```

Reset password:

```sql
ALTER USER default IDENTIFIED WITH sha256_hash BY 'hash_value';
```

Check user grants:

```sql
SHOW GRANTS FOR app_user;
```

## Examples

```sql
SELECT name, auth_type, password FROM system.users WHERE name = 'default';
```
