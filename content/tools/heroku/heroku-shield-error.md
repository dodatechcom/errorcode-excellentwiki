---
title: "[Solution] Heroku Shield Error - Fix Shield Database Connection Error"
description: "Fix Heroku Shield database connection errors for private spaces. Resolve network, firewall, and Shield-tier database issues."
tools: ["heroku"]
error-types: ["shield-error"]
severities: ["critical"]
weight: 5
---

This error means a Heroku Shield-tier database cannot establish connections. Shield databases operate in private spaces with additional network and firewall requirements.

## What This Error Means

When a Shield database connection fails, you see:

```
FATAL: no pg_hba.conf entry for host "x.x.x.x"
# or
FATAL: database system is starting up
# or
Error: connection refused to database
```

Shield databases are designed for compliance-sensitive workloads. They require VPN, Private Spaces, or specific network configurations for access.

## Why It Happens

- The client IP is not allowed in the database firewall rules
- The app is not running in the same Private Space as the database
- VPN connection is not established
- The database is restarting or in maintenance mode
- The connection pool is exhausted
- SSL connection is required but not configured

## How to Fix It

### Check database status

```bash
heroku pg:info -a my-app
```

Verify the database is available and not in a transitional state.

### Verify network configuration

```bash
heroku spaces:info -a my-app
```

Ensure the app is in a Private Space that can access the Shield database.

### Check firewall rules

```bash
heroku pg:ip-allowlist -a my-app
```

Add the client IP to the allowlist:

```bash
heroku pg:ip-allowlist:add 203.0.113.0/24 -a my-app
```

### Enable SSL connections

```python
import os
import ssl

DATABASE_URL = os.environ['DATABASE_URL']
ssl_context = ssl.create_default_ssl_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
```

### Check connection pool settings

```bash
heroku config:get DATABASE_POOL_SIZE -a my-app
```

Reduce pool size if connections are being exhausted.

### Verify DATABASE_URL

```bash
heroku config:get DATABASE_URL -a my-app
```

Ensure the URL includes `sslmode=require` for Shield databases.

### Check database credentials

```bash
heroku pg:credentials:url -a my-app
```

Regenerate credentials if they have been rotated.

### Test connectivity from within the app

```bash
heroku run python -c "import psycopg2; psycopg2.connect('$DATABASE_URL')" -a my-app
```

Testing from inside the Heroku environment verifies network access.

## Common Mistakes

- Not adding client IPs to the Shield database firewall
- Assuming Shield databases work like standard Heroku Postgres
- Forgetting that Private Spaces require VPN for external access
- Not enabling `sslmode=require` in connection strings
- Not monitoring connection pool usage before hitting limits

## Related Pages

- [Heroku Database Error]({{< relref "/tools/heroku/heroku-database-error" >}}) -- database issues
- [Heroku Config Error]({{< relref "/tools/heroku/heroku-config-error" >}}) -- configuration problems
- [Heroku API Error]({{< relref "/tools/heroku/heroku-api-error" >}}) -- API failures
