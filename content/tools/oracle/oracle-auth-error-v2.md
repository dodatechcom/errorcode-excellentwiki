---
title: "Oracle - ORA-01017: invalid username/password"
description: "Oracle rejects login attempt because the username or password is incorrect"
tools: ["oracle"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

ORA-01017: invalid username/password; logon denied occurs when Oracle cannot authenticate the user credentials. The database rejects the login attempt due to incorrect username or password.

## Common Causes

- Incorrect username or password
- Case sensitivity in password
- Account locked after too many failed attempts
- Password expired
- Schema name not included in connection string

## How to Fix

1. Verify credentials with SQL*Plus:

```bash
sqlplus username/password@mydb
```

2. Check if account is locked:

```sql
SELECT account_status, lock_date, expiry_date
FROM dba_users
WHERE username = 'MYUSER';
```

3. Unlock the account:

```sql
ALTER USER myuser ACCOUNT UNLOCK;
```

4. Reset the password:

```sql
ALTER USER myuser IDENTIFIED BY newpassword;
```

5. Check password profile settings:

```sql
SELECT * FROM dba_profiles WHERE profile = 'DEFAULT';
```

6. Verify connection string format:

```bash
# Correct format
sqlplus myuser/mypassword@//dbhost:1521/mydb

# With schema
sqlplus myuser/mypassword@mydb
```

## Examples

```bash
$ sqlplus testuser/testpass@mydb
ERROR: ORA-01017: invalid username/password; logon denied

$ sqlplus testuser/CorrectPass@mydb
Connected.
```

```sql
-- Check failed login attempts
SELECT username, failed_login_attempts, lock_date
FROM dba_users
WHERE username = 'TESTUSER';
```

## Related Errors

- [Permission error]({{< relref "/tools/oracle/oracle-permission-error" >}})
- [Connection error]({{< relref "/tools/oracle/oracle-connection-error" >}})
