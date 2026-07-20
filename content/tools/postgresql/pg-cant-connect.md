---
title: "[Solution] PostgreSQL Can't connect to server"
description: "Fix PostgreSQL 'Can't connect to server' error. Resolve connection failures when the PostgreSQL server is unreachable."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Can't connect to server

psql: error: connection to server at 'host' (IP), port 5432 failed: Connection refused

This error occurs when the PostgreSQL client cannot connect to the server. The server may not be running or a firewall may be blocking connections.

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
