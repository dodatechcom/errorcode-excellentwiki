---
title: "[Solution] PostgreSQL Partition error"
description: "Fix PostgreSQL 'partition' error. Resolve table partitioning issues."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Partition error

ERROR: cannot create partition: partitioning key column must be part of the primary key

This error occurs when the partition key is not part of the primary key.

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
