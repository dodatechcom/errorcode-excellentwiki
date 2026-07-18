---
title: "[Solution] Heroku Postgres Connection Failed — How to Fix"
description: "Fix Heroku Postgres connection errors by checking database URL config, connection limits, SSL requirements, maintenance windows, and network routing between dynos and database."
tools: ["heroku"]
error-types: ["db-error"]
severities: ["error"]
weight: 5
comments: true
---

A Heroku Postgres connection error occurs when your application cannot establish a connection to its database. This can happen due to misconfiguration, connection exhaustion, SSL/TLS issues, or database maintenance operations.

## What This Error Means

Heroku Postgres provides managed PostgreSQL databases for Heroku applications. Your application connects using the `DATABASE_URL` config var, which includes the host, port, username, password, and database name. Connection errors can occur at the network level (cannot reach the database), at the authentication level (wrong credentials), or at the application level (connection pool exhaustion).

Heroku requires SSL connections to Postgres. Applications that do not use SSL will fail with SSL-related errors. Additionally, each Heroku Postgres plan has a maximum connection limit that, when exceeded, causes new connections to be rejected.

## Why It Happens

- `DATABASE_URL` config var is missing, incorrect, or points to the wrong database
- The application exceeds the Postgres connection limit for its plan
- SSL/TLS is not configured in the database driver
- The database is in maintenance mode (planned upgrades)
- The database has reached its storage limit
- Network routing between dynos and the database is disrupted
- The database credentials have been rotated
- Connection pooling is not configured, causing excessive connections

## Common Error Messages

```
could not connect to server: Connection refused
# or
FATAL: remaining connection slots are reserved for superuser
# or
FATAL: no pg_hba.conf entry for host
# or
SSL error: connection requires a valid client certificate
```

## How to Fix It

### 1. Check Database Status

```bash
# Check database health and information
heroku pg:info -a my-app

# Ping the database
heroku pg:ping -a my-app

# Check connection count
heroku pg:connections -a my-app
```

### 2. Verify DATABASE_URL

```bash
# Check the DATABASE_URL config var
heroku config:get DATABASE_URL -a my-app

# Ensure it starts with postgres:// (not postgresql:// for some drivers)
# For Rails apps, Heroku sets it automatically when Postgres is provisioned

# If missing, add a Postgres database
heroku addons:create heroku-postgresql:mini -a my-app
```

### 3. Configure SSL in Your Application

```python
# Python (Django)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'OPTIONS': {
            'sslmode': 'require'
        }
    }
}
```

```javascript
// Node.js with pg library
const { Pool } = require('pg');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: {
    rejectUnauthorized: false
  }
});
```

```ruby
# Ruby on Rails
# In production.rb:
config.force_ssl = true
# Heroku automatically sets sslmode=require for Rails via DATABASE_URL
```

### 4. Fix Connection Pool Exhaustion

```bash
# Check current connection count
heroku pg:connections -a my-app

# Check max connections for your plan
heroku pg:info -a my-app | grep "Connections"
```

```python
# SQLAlchemy connection pool configuration
from sqlalchemy import create_engine
import os

DATABASE_URL = os.environ['DATABASE_URL']

# Standard-0 plan has 20 connections, leave some for Heroku
engine = create_engine(
    DATABASE_URL,
    pool_size=5,
    max_overflow=5,
    pool_pre_ping=True,  # Verify connections before using them
    pool_recycle=300      # Recycle connections every 5 minutes
)
```

```javascript
// Node.js pg-pool configuration
const { Pool } = require('pg');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  max: 10,           // Maximum connections in pool
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 5000
});
```

### 5. Kill Idle Connections

```bash
# View blocking queries
heroku pg:blocking -a my-app

# View locks
heroku pg:locks -a my-app

# Kill idle connections
heroku pg:killall -a my-app

# Kill a specific connection
heroku pg:kill <pid> -a my-app
```

### 6. Handle Database Maintenance

```bash
# Check if database is in maintenance
heroku pg:maintenance -a my-app

# View upcoming maintenance windows
heroku pg:info -a my-app | grep "Maintenance"

# Run maintenance manually
heroku pg:maintenance:run -a my-app

# Get maintenance window info
heroku pg:maintenance:window -a my-app
```

### 7. Upgrade Database Plan

```bash
# Check current plan
heroku pg:info -a my-app | grep "Plan"

# Upgrade to a plan with more connections
heroku addons:upgrade heroku-postgresql:standard-0 -a my-app

# Zero-downtime upgrade (creates follower, promotes it)
heroku pg:upgrade DATABASE_URL -a my-app
```

### 8. Use Connection Pooling with PgBouncer

```bash
# Enable PgBouncer for connection pooling (requires Standard plans or higher)
heroku addons:create heroku-postgresql:standard-0 -a my-app
heroku pg:connection-pooling:attach DATABASE_URL -a my-app

# Use the POOLER_URL instead of DATABASE_URL
heroku config -a my-app | grep POOLER
```

## Common Scenarios

### Connection Limit Exceeded on Hobby Plan

A Heroku Hobby Postgres plan allows 20 connections. A Puma web server with 3 workers and 8 threads each (24 total threads) creates a new connection per thread, exceeding the limit. The fix is to configure connection pooling and reduce `pool_size` to match the plan limit.

### SSL Not Configured After Migration

An application migrates from a self-hosted PostgreSQL to Heroku Postgres but does not update the database driver configuration to use SSL. The connection fails with an SSL error. Update the connection string to include `sslmode=require`.

### Database Storage Full

The application grows to exceed the 1GB limit on the Hobby plan. Writes start failing with out-of-storage errors. Upgrade to a larger plan or clean up old data, then run `VACUUM FULL` to reclaim space.

## Prevent It

- Configure connection pooling with pool limits that stay under your plan's connection max
- Use SSL mode `require` in all database driver configurations
- Monitor database storage with `heroku pg:info` and set up alerts
- Use Heroku's PgBouncer for high-connection-count applications
- Schedule maintenance windows during low-traffic periods
- Set up read replicas for read-heavy workloads
- Configure `pool_pre_ping` to detect stale connections
- Use Heroku PG Dataclips for monitoring query performance

## Related Pages

- [Heroku Config Error](/tools/heroku/heroku-config-error)
- [Heroku Dyno Error](/tools/heroku/heroku-dyno-error)
- [Heroku Release Error](/tools/heroku/heroku-release-error)
