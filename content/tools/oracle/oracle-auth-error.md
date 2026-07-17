---
title: "Oracle Authentication Error"
description: "Oracle client fails to authenticate with the database."
tools: ["oracle"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# Oracle Authentication Error

An Oracle authentication error occurs when the client cannot authenticate with the database server. The credentials are incorrect or the account is locked.

## Common Causes

- Incorrect username or password
- Account locked due to failed attempts
- Password expired
- External authentication not configured

## How to Fix

### Verify Credentials

```bash
sqlplus username/password@mydb
```

### Check Account Status

```sql
SELECT account_status FROM dba_users WHERE username = 'MYUSER';
```

### Unlock Account

```sql
ALTER USER myuser ACCOUNT UNLOCK;
```

### Reset Password

```sql
ALTER USER myuser IDENTIFIED BY new_password;
```

### Check Password Expiry

```sql
SELECT username, expiry_date FROM dba_users WHERE username = 'MYUSER';
```

### Fix External Authentication

```bash
# Check OS authentication
sqlplus / as sysdba
```

## Examples

```sql
sqlplus user/password@mydb
ERROR: ORA-01017: invalid username/password; logon denied

# Check account status
SELECT account_status FROM dba_users WHERE username = 'USER';
-- LOCKED
```

## Related Errors

- [Connection Error]({{< relref "/tools/oracle/oracle-connection-error" >}}) — connection failure
- [Permission Error]({{< relref "/tools/oracle/permission-error" >}}) — permission denied
