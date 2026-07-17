---
title: "[Solution] Docker Compose Port Conflict — Fix Port Already Allocated"
description: "Fix Docker Compose port already allocated errors. Resolve port conflicts, host binding issues, and multi-service port management."
---

## What This Error Means

The `port is already allocated` error means another process or container is already using the host port that Docker Compose is trying to bind to.

A typical error:

```
Error response from daemon: driver failed programming external connectivity
on endpoint web (abc123): Bind for 0.0.0.0:80: address already in use
```

Or:

```
Error starting userland proxy: listen tcp4 0.0.0.0:443: bind: address already in use
```

## Why It Happens

Port conflicts occur when:

- **Another container uses the same port**: A previously started container still holds the port.
- **Host service using the port**: Nginx, Apache, or another service is running on the same port.
- **Stale Docker network**: Old network configuration retains port bindings.
- **Multiple compose projects**: Different compose files bind to the same host ports.
- **TIME_WAIT state**: Recently closed connections leave ports in TIME_WAIT state.

## How to Fix It

**Step 1: Find what is using the port**

```bash
sudo lsof -i :80
sudo netstat -tlnp | grep :80
# Or for all platforms
docker ps --format "table {{.Names}}\t{{.Ports}}"
```

**Step 2: Stop the conflicting container**

```bash
docker stop $(docker ps -q --filter "publish=80")
```

**Step 3: Use different host ports**

```yaml
services:
  web:
    ports:
      - "8080:80"  # Map host port 8080 to container port 80
      - "8443:443"
```

**Step 4: Use dynamic port assignment**

```yaml
services:
  web:
    ports:
      - "80"  # Docker assigns a random available host port
```

Find the assigned port:

```bash
docker compose port web 80
```

**Step 5: Stop all compose services and clean networks**

```bash
docker compose down --remove-orphans
docker network prune
```

**Step 6: Use `host.docker.internal` for host services**

```yaml
services:
  web:
    extra_hosts:
      - "host.docker.internal:host-gateway"
```

## Common Mistakes

- **Using common ports like 80 and 443**: Map to high-numbered ports on the host to avoid conflicts.
- **Not cleaning up after previous runs**: Always run `docker compose down` before starting new instances.
- **Hardcoding host ports in compose files**: Use environment variables for port configuration across environments.
- **Ignoring `--remove-orphans`**: Orphaned containers from previous compose runs cause hidden conflicts.

## Related Pages

- [Docker Compose Network Error](/tools/docker-compose/docker-compose-network-error/) — Network connectivity issues
- [Docker Compose Build Error](/tools/docker-compose/docker-compose-build-error/) — Image build failures
- [Ansible Connection Refused](/tools/ansible/ansible-connection-refused/) — SSH connection issues
