---
title: "[Solution] Docker Compose Dependency Service Failed Error — How to Fix"
description: "Fix Docker Compose dependency service failed to start errors. Resolve depends_on failures, startup ordering, and health check dependency issues."
comments: true
---

## What This Error Means

The `dependency service failed to start` error occurs when a service that another service depends on fails to start or become healthy. Docker Compose cannot proceed with starting the dependent service because its prerequisite is not in the expected state.

A typical error:

```
ERROR: for web  Cannot start service web:
dependency "db" failed to start: container db exited (1)
```

Or:

```
Error response from daemon: Could not connect to Redis
at redis://cache:6379: Connection refused
```

Or:

```
ERROR: for api  Depends on service "db" which is unhealthy
```

Or:

```
Service "worker" depends on service "api" which service
is undefined. Did you mean api?
```

## Why It Happens

Dependency failures occur when:

- **Prerequisite service crashes**: The dependency service starts but immediately exits due to a configuration error.
- **Health check not passing**: The dependent service waits for a health check that never returns healthy.
- **Database not ready**: The application starts before the database has finished initializing, causing connection refused errors.
- **Network not available**: Services on different networks cannot communicate because they were not connected properly.
- **Resource exhaustion**: The dependency service consumes all available memory or CPU and is killed by the OOM killer.
- **Configuration typo**: The service name in `depends_on` does not match any service defined in the compose file.

## Common Error Messages

### Service exited before dependency started

```
ERROR: for web  Cannot start service web:
dependency "db" failed to start: container db_1 exited (1)
```

The database container started but crashed before the web service could connect.

### Health check dependency not met

```
ERROR: for api  Depends on service "db" which is unhealthy
```

Compose waits for the database to be healthy, but the health check never succeeds within the timeout period.

### Service name typo in depends_on

```
ERROR: Service "api" depends on service "database"
which is undefined. Did you mean db?
```

The compose file references a service name that does not exist. A simple spelling mistake causes the dependency graph to be invalid.

### Cascading dependency failure

```
ERROR: for worker  Cannot start service worker:
dependency "api" failed to start: dependency "db"
failed to start: dependency "cache" failed to start
```

A chain of dependencies fails when the last service in the chain crashes first.

## How to Fix It

### Solution 1: Use depends_on with health checks

Wait for the dependency to be healthy, not just started.

```yaml
services:
  db:
    image: postgres:16
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5

  api:
    image: myapi:latest
    depends_on:
      db:
        condition: service_healthy
    environment:
      DATABASE_URL: postgres://postgres:password@db:5432/mydb
```

### Solution 2: Implement application-level retry logic

Do not rely solely on Compose dependencies. Add retry logic in the application code.

```python
# Python example with tenacity retry
import time
import psycopg2
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(10), wait=wait_exponential(multiplier=1, min=1, max=30))
def get_db_connection():
    return psycopg2.connect(
        host="db",
        port=5432,
        dbname="mydb",
        user="postgres",
        password="password"
    )
```

```javascript
// Node.js example with retry logic
const retry = require('async-retry');
const { Pool } = require('pg');

const pool = new Pool({
  host: 'db',
  port: 5432,
  database: 'mydb',
  user: 'postgres',
  password: 'password',
});

async function connectWithRetry() {
  return retry(async () => {
    await pool.query('SELECT 1');
    console.log('Database connected');
  }, {
    retries: 10,
    minTimeout: 1000,
    maxTimeout: 30000,
  });
}
```

### Solution 3: Add an entrypoint wait script

Use a wait-for-it script to block the dependent service until the dependency is ready.

```yaml
services:
  api:
    image: myapi:latest
    depends_on:
      - db
      - cache
    entrypoint: ["./wait-for-it.sh", "db:5432", "cache:6379", "--"]
    command: ["python", "manage.py", "runserver"]
```

Create a lightweight wait script:

```bash
#!/bin/bash
# wait-for-it.sh
HOST=$1
PORT=$2
TIMEOUT=${3:-30}

echo "Waiting for $HOST:$PORT (timeout: ${TIMEOUT}s)..."
for i in $(seq 1 $TIMEOUT); do
  if nc -z "$HOST" "$PORT" 2>/dev/null; then
    echo "$HOST:$PORT is available"
    exit 0
  fi
  sleep 1
done

echo "Timeout reached: $HOST:$PORT not available"
exit 1
```

### Solution 4: Fix the dependency graph

Verify all service references exist and the dependency chain is correct.

```yaml
# WRONG - "database" is not a defined service
services:
  api:
    depends_on:
      - database

  db:
    image: postgres:16

# CORRECT - reference the actual service name
services:
  api:
    depends_on:
      - db

  db:
    image: postgres:16
```

Validate the compose file:

```bash
docker compose config --services
# Lists all defined service names

docker compose config
# Shows the full resolved configuration including dependency graph
```

### Solution 5: Increase startup timeouts

Health check retries and intervals may be too aggressive. Give services more time to start.

```yaml
services:
  db:
    image: postgres:16
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s      # Increased from 5s
      timeout: 10s        # Increased from 5s
      retries: 10         # Increased from 5
      start_period: 30s   # Grace period during startup

  api:
    depends_on:
      db:
        condition: service_healthy
```

## Common Scenarios

### Database not initialized on first run

On the first `docker compose up`, the database container needs time to create schemas, run migrations, and seed data. The application starts before this completes.

```yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_DB: mydb
      POSTGRES_PASSWORD: password
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres -d mydb"]
      interval: 5s
      timeout: 5s
      retries: 10

  api:
    image: myapi:latest
    depends_on:
      db:
        condition: service_healthy
    command: >
      sh -c "python manage.py migrate &&
             python manage.py runserver 0.0.0.0:8000"
```

### Redis cache not ready

Redis starts quickly but may not be ready to accept connections immediately, especially with persistence enabled.

```yaml
services:
  cache:
    image: redis:7-alpine
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 3s
      timeout: 3s
      retries: 5

  api:
    depends_on:
      cache:
        condition: service_healthy
```

### Circular dependency between services

Two services that depend on each other create an impossible startup order.

```yaml
# WRONG - circular dependency
services:
  api:
    depends_on:
      - worker
  worker:
    depends_on:
      - api

# CORRECT - remove circular dependency
services:
  api:
    image: myapi:latest
    depends_on:
      - db
  worker:
    image: myworker:latest
    depends_on:
      - db
```

## Prevent It

- **Always use health checks with depends_on**: The `service_healthy` condition is far more reliable than `service_started`. A service can start and immediately crash, but a health check confirms it is actually ready to accept connections.
- **Add application-level resilience**: Do not depend only on Compose startup ordering. Implement connection retry logic in your application so it can recover from temporary unavailability at any point during its lifecycle, not just at startup.
- **Map out the dependency graph visually**: Before writing the compose file, sketch the service dependencies. This reveals circular dependencies, missing services, and unnecessary coupling that cause runtime failures.
