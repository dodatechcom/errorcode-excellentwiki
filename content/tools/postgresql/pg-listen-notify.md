---
title: "[Solution] PostgreSQL LISTEN/NOTIFY error"
description: "Fix PostgreSQL 'LISTEN/NOTIFY' error. Resolve asynchronous notification issues."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL LISTEN/NOTIFY error

ERROR: cannot LISTEN while not in normal query processing

This error occurs when LISTEN is used in an invalid context.

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
