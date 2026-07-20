---
title: "[Solution] PostgreSQL Reserved connections error"
description: "Fix PostgreSQL 'reserved connections' error. Resolve superuser connection reservation issues."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Reserved connections error

FATAL: remaining connection slots are reserved for non-replication superuser connections

This error occurs when regular connections exceed the limit minus superuser_reserved_connections.

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
