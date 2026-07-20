---
title: "[Solution] PostgreSQL Unique constraint violation"
description: "Fix PostgreSQL 'unique constraint violation' error. Resolve duplicate value issues."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Unique constraint violation

ERROR: duplicate key value violates unique constraint '<constraint>'

This error occurs when an INSERT or UPDATE creates a duplicate value in a unique column.

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
