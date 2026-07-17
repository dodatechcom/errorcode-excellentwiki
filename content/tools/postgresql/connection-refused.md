---
title: "FATAL: connection refused (check pg_hba.conf)"
description: "PostgreSQL refuses client connections due to authentication or configuration issues in pg_hba.conf"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

This error occurs when PostgreSQL rejects a client connection attempt, typically because the client is not authorized to connect from their host or the server is not configured to accept connections.

## Common Causes

- Client IP address is not listed in `pg_hba.conf`
- Authentication method mismatch in `pg_hba.conf`
- PostgreSQL server is listening on wrong interface/port
- Firewall blocking the connection

## How to Fix

1. Edit `pg_hba.conf` to add your client's IP:

```bash
# Add this line to pg_hba.conf
host    all    all    192.168.1.0/24    md5
```

2. Reload PostgreSQL configuration:

```sql
SELECT pg_reload_conf();
```

3. Verify the server is listening on the correct interface:

```bash
ss -tlnp | grep 5432
```

## Examples

```sql
-- This will fail if pg_hba.conf doesn't allow your IP
psql -h 192.168.1.100 -U myuser -d mydb

-- Error output:
-- FATAL: connection refused (check pg_hba.conf)
```

```bash
# Testing connection from command line
psql -h localhost -U postgres
# FATAL: connection refused (check pg_hba.conf)
```

## Related Errors

- [Database Already Exists](/tools/postgresql/database-exists)
