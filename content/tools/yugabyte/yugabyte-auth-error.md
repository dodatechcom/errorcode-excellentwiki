---
title: "[Solution] YugabyteDB Authentication Error — How to Fix"
description: "Fix YugabyteDB authentication errors by configuring YSQL auth, resolving password issues, and fixing role-based access control"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Authentication Error

YugabyteDB authentication errors occur when clients fail to authenticate or lack permissions. YugabyteDB supports PostgreSQL-compatible authentication via pg_hba.conf.

## Why It Happens

- pg_hba.conf rejects client connections
- Password is incorrect for the user
- User does not exist in the database
- Authentication method is misconfigured
- SSL client certificate is not provided
- Role does not have required privileges

## Common Error Messages

```
FATAL: password authentication failed for user "yugabyte"
```

```
FATAL: pg_hba.conf rejects connection
```

```
ERROR: permission denied for table
```

```
FATAL: role "app_user" does not exist
```

## How to Fix It

### 1. Configure Authentication

```bash
# Edit pg_hba.conf
# Located at: /home/yugabyte/yugabyte-data/master/pg_hba.conf

# Allow password auth from local network
# host all all 10.0.0.0/8 md5

# Allow trust for development (NOT for production)
# host all all 0.0.0.0/0 trust
```

### 2. Create Users and Roles

```sql
-- Create user
CREATE USER app_user WITH PASSWORD 'secure_password';

-- Create role
CREATE ROLE read_only;

-- Grant privileges
GRANT CONNECT ON DATABASE mydb TO app_user;
GRANT USAGE ON SCHEMA public TO app_user;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO app_user;

-- Grant role to user
GRANT read_only TO app_user;
```

### 3. Fix Password Issues

```sql
-- Reset user password
ALTER USER app_user WITH PASSWORD 'new_password';

-- Check user exists
SELECT usename FROM pg_user WHERE usename = 'app_user';
```

### 4. Configure Auth Method

```bash
# In tserver.gflags, set auth method:
--ysql_hba_conf_csv=host all all 0.0.0.0/0 md5

# For cert auth:
--ysql_enable_auth=true
--ysql_hba_conf_csv=hostssl all all 0.0.0.0/0 cert
```

## Common Scenarios

- **New installation allows any access**: Configure pg_hba.conf before exposing to network.
- **Application cannot authenticate**: Ensure password matches and pg_hba.conf allows the connection.
- **Role permission denied**: Grant appropriate privileges to the role.

## Prevent It

- Configure authentication before exposing cluster to network
- Use least-privilege roles for applications
- Monitor failed authentication attempts

## Related Pages

- [YugabyteDB Connection Error](/tools/yugabyte/yugabyte-connection-error)
- [YugabyteDB SSL Error](/tools/yugabyte/yugabyte-ssl-error)
- [YugabyteDB Auth Error](/tools/yugabyte/yugabyte-auth-error)
