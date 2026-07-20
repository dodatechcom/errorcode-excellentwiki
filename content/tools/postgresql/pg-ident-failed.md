---
title: "[Solution] PostgreSQL Ident authentication failed"
description: "Fix PostgreSQL 'ident authentication failed' error. Resolve authentication failures with ident/auth methods."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Ident authentication failed

FATAL: ident authentication failed for user 'user'

This error occurs when PostgreSQL uses ident authentication and the operating system user does not match the database user.

## How to Fix

### Check PostgreSQL Status

```bash
sudo systemctl status postgresql
pg_isready
```

### Check PostgreSQL Logs

```bash
sudo tail -100 /var/log/postgresql/postgresql-*-main.log
```

### Verify pg_hba.conf

```bash
sudo cat /etc/postgresql/*/main/pg_hba.conf
```

## Related Errors

- [Connection Refused]({{< relref "/tools/postgresql/pg-connection-refused" >}}) — server unreachable
- [Database Does Not Exist]({{< relref "/tools/postgresql/pg-database-does-not-exist" >}}) — missing database
