---
title: "[Solution] Docker Compose Upstream Error — Fix Connect Error"
description: "Fix Docker Compose upstream connect error. Resolve proxy issues, container startup timing, and upstream service connectivity problems."
---

## What This Error Means

The `upstream connect error` means a container acting as a reverse proxy or client cannot establish a connection to an upstream service. This is common with Nginx, Traefik, and application containers that depend on backend services.

A typical error:

```
upstream connect error or disconnect/reset before headers. reset reason:
connection failure
```

Or:

```
nginx: [emerg] host not found in upstream "api" in /etc/nginx/conf.d/default.conf:5
```

## Why It Happens

Upstream errors occur when:

- **Upstream service not started yet**: The client container starts before the upstream service is ready.
- **DNS resolution failure**: The service name used as upstream cannot be resolved.
- **Network isolation**: The upstream container is on a different Docker network.
- **Port mismatch**: The upstream container exposes a different port than the client expects.
- **Health check missing**: No health checks ensure the upstream is ready before client starts.
- **Proxy misconfiguration**: Nginx or other proxy configuration references wrong service names.

## How to Fix It

**Step 1: Add health checks to upstream services**

```yaml
services:
  api:
    image: node:18
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s
```

**Step 2: Use depends_on with condition**

```yaml
services:
  web:
    image: nginx
    depends_on:
      api:
        condition: service_healthy
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
```

**Step 3: Add retry logic in application code**

```python
# Python example with retry
import time
import requests

for attempt in range(10):
    try:
        response = requests.get("http://api:3000/health")
        if response.status_code == 200:
            break
    except requests.ConnectionError:
        pass
    time.sleep(5)
```

**Step 4: Use a startup script with wait**

```yaml
services:
  web:
    image: nginx
    entrypoint: /bin/sh
    command: >
      -c "sleep 10 && nginx -g 'daemon off;'"
```

**Step 5: Verify network connectivity**

```bash
# Test from inside the container
docker compose exec web nslookup api
docker compose exec web curl -v http://api:3000/health

# Check which networks each service is on
docker network inspect <project>_default
```

**Step 6: Fix Nginx upstream configuration**

```nginx
# /etc/nginx/conf.d/default.conf
upstream api_backend {
    server api:3000;  # Use service name, not IP
}

server {
    listen 80;
    location /api/ {
        proxy_pass http://api_backend;
        proxy_connect_timeout 10s;
        proxy_read_timeout 30s;
    }
}
```

## Common Mistakes

- **Not adding health checks for service dependencies**: Always use health checks with `depends_on` condition.
- **Using container IPs instead of service names**: Container IPs change. Always use Docker service names.
- **Starting all services simultaneously**: Use `depends_on` to enforce startup order.
- **Not accounting for application startup time**: Some applications take 30+ seconds to start. Adjust health check intervals accordingly.

## Related Pages

- [Docker Compose Network Error](/tools/docker-compose/docker-compose-network-error/) — Network connectivity issues
- [Docker Compose Port Conflict](/tools/docker-compose/docker-compose-port-conflict/) — Port binding issues
- [Kubectl Connection Refused](/tools/kubectl/kubectl-connection-refused/) — API server connectivity
