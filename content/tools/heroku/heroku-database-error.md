---
title: "[Solution] Heroku Too Many Connections Error — Fix Database Connection Limits"
description: "Fix Heroku database too many connections errors. Resolve connection pool exhaustion and database connection management."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
weight: 6
---

A Heroku too many connections error occurs when your application exceeds the database connection limit. Heroku Postgres has per-plan connection limits, and exceeding them causes connection failures.

## What This Error Means

```
FATAL: too many connections for role "..."
FATAL: remaining connection slots are reserved for non-replication superuser connections
```

Your application has opened more database connections than the database plan allows.

Connection limits by plan:

- **Mini**: 20 connections
- **Basic**: 20 connections
- **Standard-0**: 120 connections
- **Standard-1**: 120 connections
- **Premium-0**: 120 connections

## Why It Happens

- Connection pool not configured correctly
- Multiple dynos each opening connections
- Connections not being released back to the pool
- Each serverless invocation creates new connections
- Database connections leak due to unhandled errors

## How to Fix It

### Configure Connection Pool

```javascript
// Node.js with pg-pool
const { Pool } = require('pg');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  max: 5,           // Max connections per dyno
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 2000,
});

// Calculate: max_connections / number_of_dynos = connections_per_dyno
```

### Use Heroku-Recommended Pool Size

```javascript
// For Standard-1X dynos
// Total connections: 20 (mini) or 120 (standard)
// Safe per dyno: total / (dynos + 1)

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  max: 5,
  min: 2,
});
```

### Release Connections Properly

```javascript
// WRONG: Connection not released on error
app.get('/users', async (req, res) => {
  const client = await pool.connect();
  const result = await client.query('SELECT * FROM users');
  res.json(result.rows);
  // Connection leaked if query throws!
});

// RIGHT: Always release in finally block
app.get('/users', async (req, res) => {
  const client = await pool.connect();
  try {
    const result = await client.query('SELECT * FROM users');
    res.json(result.rows);
  } finally {
    client.release();
  }
});
```

### Check Current Connections

```bash
# View active connections
heroku pg:info

# Connect to database and check
heroku pg:psql

# Run in psql:
SELECT count(*) FROM pg_stat_activity;
SELECT usename, state FROM pg_stat_activity;
```

### Kill Idle Connections

```bash
# Terminate idle connections
heroku pg:psql

# In psql:
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE state = 'idle'
  AND query_start < now() - interval '10 minutes';
```

### Use Connection Pooling with PgBouncer

```bash
# Heroku includes PgBouncer
# Enable it via Dashboard > Resources > Heroku Postgres > Settings

# Or use external connection pooler
heroku addons:create heroku-redis:hobby-dev
```

### Optimize Connection Usage

```javascript
// Reuse pool across requests
// Do NOT create new pool per request
const pool = require('./db'); // Module-level pool

app.get('/users', async (req, res) => {
  const { rows } = await pool.query('SELECT * FROM users');
  res.json(rows);
});
```

## Common Mistakes

- Creating a new database connection per request
- Not configuring pool max size
- Not releasing connections after errors
- Running too many dynos without adjusting pool size
- Not monitoring connection count

## Related Pages

- [Heroku Dyno Error]({{< relref "/tools/heroku/heroku-dyno-error" >}}) — R14 Memory quota exceeded
- [Heroku Config Error]({{< relref "/tools/heroku/heroku-config-error" >}}) — Config var not set
