---
title: "[Solution] Heroku Dyno Crashed or Restarted — How to Fix"
description: "Fix Heroku dyno crashes and restarts by analyzing R14/R15 memory errors, checking application logs, adjusting dyno sizing, and fixing unhandled exceptions in your code."
tools: ["heroku"]
error-types: ["dyno-error"]
severities: ["error"]
weight: 5
comments: true
---

A Heroku dyno crash or restart occurs when a dyno process exits unexpectedly. Heroku automatically restarts crashed dynos, but frequent crashes impact application availability and performance.

## What This Error Means

Heroku runs your application in lightweight containers called dynos. Each dyno type has memory and CPU limits. When a dyno crashes, Heroku logs the exit code and restarts it automatically. Common crash reasons include out-of-memory errors, unhandled exceptions, and SIGTERM/SIGKILL signals from the platform.

Dyno restarts fall into two categories: intentional (scale-up, deploys, config var changes) and unintentional (crashes, OOM kills). Unintentional restarts indicate underlying application issues that need debugging.

## Why It Happens

- Out-of-memory (R14/R15) errors cause the dyno to be killed by the platform
- Unhandled exceptions or segmentation faults crash the application process
- The web server crashes due to port binding issues
- Database connection pool exhaustion causes request failures
- Long-running requests trigger dyno timeouts (30 seconds for web dynos)
- Health check failures cause repeated restarts
- Memory leaks accumulate over time until the dyno is killed
- The application processes too many concurrent requests for the dyno size

## Common Error Messages

```
Error R14 (Memory quota exceeded)
# or
Error R15 (Memory quota vastly exceeded) — Process killed
# or
State changed from up to crashed — Exit code 137
# or
at=error code=H13 desc="Connection closed without response"
```

## How to Fix It

### 1. Analyze Crash Logs

```bash
# View recent dyno crashes
heroku logs --tail -a my-app | grep -E "(Error|crash|killed|exit)"

# Check for specific error codes
heroku logs -a my-app | grep "Error R14"
heroku logs -a my-app | grep "Error R15"

# View the full log for the crashed dyno
heroku logs -a my-app --dyno web.1
```

### 2. Fix Memory Issues (R14/R15)

```bash
# Check current memory usage
heroku ps:stats -a my-app

# Upgrade to a larger dyno type
heroku ps:type web=standard-2x -a my-app

# Or add more dynos and use a max memory configuration
heroku ps:scale web=3 -a my-app
```

```python
# In your application, configure memory limits
# For Node.js:
# node --max-old-space-size=512 server.js

# For Python/Gunicorn:
# gunicorn --workers 2 --max-requests 1000 app:app

# For Java:
# java -Xmx256m -jar app.jar
```

### 3. Fix Unhandled Exceptions

```python
import logging
import sys

logger = logging.getLogger(__name__)

# Add global exception handler
def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logger.critical("Unhandled exception", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_exception
```

### 4. Optimize Database Connection Pooling

```python
# Django example — configure connection pool
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'CONN_MAX_AGE': 300,  # Reuse connections for 5 minutes
        'OPTIONS': {
            'pool': {
                'min_size': 1,
                'max_size': 5,  # Match dyno concurrency
            }
        }
    }
}

# SQLAlchemy example
from sqlalchemy import create_engine
engine = create_engine(
    DATABASE_URL,
    pool_size=5,
    max_overflow=0,
    pool_pre_ping=True
)
```

### 5. Handle SIGTERM Gracefully

```python
import signal
import sys

def handle_sigterm(signum, frame):
    print("Received SIGTERM, shutting down gracefully")
    # Close database connections
    # Finish in-flight requests
    # Clean up resources
    sys.exit(0)

signal.signal(signal.SIGTERM, handle_sigterm)
```

### 6. Optimize Web Server Configuration

```python
# Gunicorn configuration for Heroku
# gunicorn_conf.py
import multiprocessing

bind = "0.0.0.0:{}".format(os.environ.get('PORT', '8000'))
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
timeout = 30
keepalive = 5
max_requests = 1000
max_requests_jitter = 50
```

```bash
# Run with optimized config
heroku ps:type web=standard-1x -a my-app
```

### 7. Debug with One-Off Dynos

```bash
# Run a bash session to debug interactively
heroku run bash -a my-app

# Check memory and processes
top -b -n 1 | head -20
ps aux --sort=-%mem | head -10

# Test database connectivity
heroku pg:ping -a my-app
```

## Common Scenarios

### Memory Leak in a Background Job

A Sidekiq worker processes image uploads but never releases memory after each job. After processing 1000 images, the dyno exceeds its memory quota and gets killed by R15. The fix is to add `GC.start` after each job or use a memory-profiling tool to find the leak.

### Unhandled Promise Rejection in Node.js

A Node.js API endpoint makes an external HTTP call with `.catch()` missing on some code paths. When the external service is slow, the unhandled rejection crashes the Node process and the dyno exits. Add a global `unhandledRejection` handler to prevent crashes.

### Database Connection Exhaustion

A Rails app uses the default Puma configuration with 5 workers and 16 threads per worker (80 total threads). Each thread opens a database connection. Heroku Postgres allows only 20 connections on the Standard-0 plan. Threads block waiting for connections, requests time out, and the dyno restarts. Reduce thread count to match database connection limits.

## Prevent It

- Use a dyno type appropriate for your application's memory footprint
- Set memory limits in your runtime (e.g., `NODE_OPTIONS="--max-old-space-size=512"`)
- Implement graceful shutdown handlers for SIGTERM
- Monitor dyno memory with `heroku ps:stats` and set up alerts
- Configure connection pools to match database connection limits
- Use the Puma web server with thread-safe configuration
- Add global exception handlers in your application
- Test dyno behavior with load testing tools before production deployment

## Related Pages

- [Heroku Router Error](/tools/heroku/heroku-router-error)
- [Heroku Release Error](/tools/heroku/heroku-release-error)
- [Heroku DB Error](/tools/heroku/heroku-db-error)
