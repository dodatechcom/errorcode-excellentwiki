---
title: "[Solution] Docker Compose Health Check Failed Error — How to Fix"
description: "Fix Docker Compose container health check failed errors. Resolve unhealthy status, healthcheck timeout, and startup probe failures now."
comments: true
---

## What This Error Means

The `container health check failed` error occurs when a Docker container's health check probe reports the container as `unhealthy`. Docker marks the container after the health check fails for the configured number of retries, which can cause dependent services to fail.

A typical error:

```
ERROR: for web  Depends on service "api" which is unhealthy
```

Or:

```
Health: unhealthy
- error: Get "http://localhost:8080/health":
dial tcp 127.0.0.1:8080: connect: connection refused
```

Or:

```
Container myservice  Unhealthy
Exit code: 1
```

Or:

```
service "web" is unhealthy: "api" failed to reach
healthy state within 30s timeout
```

## Why It Happens

Health check failures occur when:

- **Application not ready**: The container started but the application inside has not finished initializing.
- **Wrong health check endpoint**: The health check URL or command points to a non-existent path.
- **Port mismatch**: The health check probes a different port than the application listens on.
- **Application crashing**: The process exits or enters an error state that prevents responding to health probes.
- **Resource starvation**: The container has insufficient memory or CPU to respond to health checks.
- **Dependencies not met**: The application needs a database or cache that is not yet available.
- **Health check too aggressive**: Intervals and timeouts are too short for the application startup time.

## Common Error Messages

### Connection refused on health endpoint

```
Health: unhealthy
- error: Get "http://localhost:8080/health":
dial tcp 127.0.0.1:8080: connect: connection refused
```

The application has not started listening on the expected port yet.

### Health check command failed

```
Health: unhealthy
- error: exit status 1:
curl: (7) Failed to connect to localhost port 3000
```

A curl-based health check cannot reach the application because the process is not running or the port is wrong.

### Timeout exceeded

```
Health: unhealthy
- error: context deadline exceeded
```

The health check takes too long to respond, exceeding the configured timeout.

### Dependency waiting for health

```
ERROR: for worker  Service "worker" depends on service "api"
which is unhealthy
```

A downstream service cannot start because its dependency never becomes healthy.

## How to Fix It

### Solution 1: Configure proper health check timing

Give the application enough time to start before health checks begin failing.

```yaml
services:
  api:
    image: myapi:latest
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s
```

The `start_period` gives the application a grace period. Failed checks during this period do not count toward the retry limit.

### Solution 2: Fix the health check endpoint

Ensure the health check targets a valid endpoint that actually returns a success status.

```bash
# Test the health endpoint manually inside the container
docker compose exec api curl -v http://localhost:8080/health

# Common health endpoints to try
curl http://localhost:8080/health
curl http://localhost:8080/healthz
curl http://localhost:8080/api/status
curl http://localhost:8080/ping
```

```yaml
services:
  api:
    image: myapi:latest
    healthcheck:
      # CORRECT - endpoint that actually exists
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      # WRONG - endpoint does not exist
      # test: ["CMD", "curl", "-f", "http://localhost:8080/healthcheck"]
```

### Solution 3: Use alternative health check methods

If curl is not available in the container, use other approaches.

```yaml
services:
  api:
    image: myapi:latest
    healthcheck:
      # Option A: wget (available in most Linux images)
      test: ["CMD", "wget", "--spider", "-q", "http://localhost:8080/health"]

      # Option B: netcat for TCP-based checks
      test: ["CMD-SHELL", "nc -z localhost 8080 || exit 1"]

      # Option C: Application-specific command
      test: ["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8080/health')"]

      # Option D: Node.js health check
      test: ["CMD", "node", "-e", "require('http').get('http://localhost:8080/health', (r) => process.exit(r.statusCode === 200 ? 0 : 1))"]
```

### Solution 4: Add a dedicated health check endpoint to the application

Create a simple health endpoint that does not depend on external resources.

```python
# Flask example
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200
```

```javascript
// Express.js example
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'ok' });
});
```

```go
// Go example
http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
    w.WriteHeader(http.StatusOK)
    json.NewEncoder(w).Encode(map[string]string{"status": "ok"})
})
```

### Solution 5: Remove or disable problematic health checks

During development, health checks may not be necessary.

```yaml
services:
  api:
    image: myapi:latest
    # Disable health check for local development
    healthcheck:
      disable: true
```

Or set unlimited retries for development:

```yaml
services:
  api:
    image: myapi:latest
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 5s
      timeout: 3s
      retries: 999
      start_period: 60s
```

## Common Scenarios

### Application needs time to run migrations

The health check starts before database migrations complete, causing premature unhealthy status.

```yaml
services:
  api:
    image: myapi:latest
    command: >
      sh -c "python manage.py migrate &&
             python manage.py runserver 0.0.0.0:8000"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 10s
      timeout: 5s
      retries: 20
      start_period: 120s
    depends_on:
      db:
        condition: service_healthy
```

### Container crashes after passing health check

The container becomes healthy, then crashes due to a delayed error. This causes cascading failures in dependent services.

```yaml
services:
  api:
    image: myapi:latest
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 10s
      timeout: 5s
      retries: 3
    restart: on-failure:5
```

### Health check fails in production but works locally

Production has stricter resource limits or different environment variables that affect application startup.

```yaml
services:
  api:
    image: myapi:latest
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: "1.0"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 15s
      timeout: 10s
      retries: 5
      start_period: 60s
    environment:
      - JAVA_OPTS=-Xms256m -Xmx512m
```

## Prevent It

- **Always include start_period in health checks**: The `start_period` parameter tells Docker to ignore health check failures during application startup. Set it to the maximum time your application needs to fully initialize, including any migrations or cache warming.
- **Test health checks against production-like environments**: Run the compose stack with production-equivalent resource limits and environment variables in CI. Health checks that pass locally with unlimited resources often fail under production constraints.
- **Implement a dedicated health endpoint in every service**: Do not rely on generic endpoints like `/` or `/index.html`. A dedicated `/health` endpoint that returns a simple JSON response is fast, lightweight, and gives you precise control over what constitutes a healthy state.
