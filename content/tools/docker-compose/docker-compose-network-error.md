---
title: "[Solution] Docker Compose Network Error — Fix Service Connection"
description: "Fix Docker Compose could not connect to service errors. Resolve DNS resolution, network isolation, and container connectivity problems."
---

## What This Error Means

The `could not connect to service` error means containers within the same Docker Compose project cannot reach each other over the network. Service discovery or network configuration is misconfigured.

A typical error:

```
web_1 | curl: (6) Could not resolve host: api
```

Or:

```
web_1 | Error: connect ECONNREFUSED 172.18.0.3:3000
```

## Why It Happens

Network errors occur when:

- **Services in different networks**: Containers are on separate Docker networks and cannot communicate.
- **Service name DNS failure**: The service name used in requests does not match the compose service name.
- **Port mismatch**: The client connects to the wrong port on the target service.
- **Service not ready**: The target service has not finished starting when the client tries to connect.
- **Custom network configuration**: Manually created networks interfere with compose networking.
- **Host networking mode**: Containers using `network_mode: host` bypass Docker DNS.

## How to Fix It

**Step 1: Verify services are on the same network**

```bash
docker network ls
docker network inspect <project>_default
```

**Step 2: Use service names for inter-container communication**

```yaml
services:
  web:
    image: nginx
    depends_on:
      - api
  api:
    image: node:18
    # Web connects to "api" using the service name
```

```yaml
# In web container config or environment
API_URL=http://api:3000
```

**Step 3: Define a custom network**

```yaml
services:
  web:
    networks:
      - frontend
  api:
    networks:
      - frontend
      - backend
  db:
    networks:
      - backend

networks:
  frontend:
  backend:
```

**Step 4: Add health checks and depends_on with condition**

```yaml
services:
  web:
    depends_on:
      api:
        condition: service_healthy
  api:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 10s
      timeout: 5s
      retries: 3
```

**Step 5: Verify DNS resolution from inside a container**

```bash
docker compose exec web nslookup api
docker compose exec web curl -v http://api:3000/health
```

## Common Mistakes

- **Using `localhost` or `127.0.0.1` for other containers**: Always use the service name, not localhost.
- **Forgetting that Docker DNS takes time to propagate**: Add health checks and retry logic.
- **Mixing network modes**: Do not use `network_mode: host` and custom networks together.
- **Not defining explicit networks**: Default networks work for simple setups but custom networks provide better isolation.

## Related Pages

- [Docker Compose Port Conflict](/tools/docker-compose/docker-compose-port-conflict/) — Port binding issues
- [Docker Compose Volume Error](/tools/docker-compose/docker-compose-volume-error/) — Volume mount failures
- [Kubectl Connection Refused](/tools/kubectl/kubectl-connection-refused/) — API server connectivity
