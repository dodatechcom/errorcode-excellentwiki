---
title: "[Solution] Docker Compose Port Already Allocated Error — How to Fix"
description: "Fix Docker Compose port already allocated errors. Resolve host port binding failures, conflicts between services, and allocation issues."
comments: true
---

## What This Error Means

The `port already allocated` error means the host port Docker Compose is trying to bind is already in use by another process or container. Docker cannot assign the same host port to two different services simultaneously.

A typical error:

```
Error response from daemon: driver failed programming external connectivity
on endpoint myservice (abc123def): Bind for 0.0.0.0:3000:
address already in use
```

Or:

```
Error starting userland proxy: listen tcp4 0.0.0.0:5432:
bind: address already in use
```

Or:

```
Bind for 0.0.0.0:8080 failed: port is already allocated
```

Or:

```
ERROR: for myservice_1  Cannot start service web:
driver failed programming external connectivity
on endpoint myservice_1: Ports are not available:
8080 port is already allocated
```

## Why It Happens

Port allocation errors occur when:

- **Previous container still running**: A container from a previous `docker compose up` is still bound to the port.
- **Host service occupying the port**: Nginx, Apache, PostgreSQL, or another system service is running on the same port.
- **Orphaned containers**: Containers created by Docker Compose but not properly cleaned up hold port bindings.
- **Multiple compose projects**: Two or more compose files in different directories bind to the same host port.
- **TIME_WAIT socket state**: Recently closed connections leave ports in a lingering TCP state that prevents immediate reuse.
- **Rapid restart cycles**: Stopping and restarting services too quickly causes a race condition where the old binding has not fully released.

## Common Error Messages

### Primary port conflict

```
Error response from daemon: driver failed programming external
connectivity on endpoint web (abc123): Bind for 0.0.0.0:80:
address already in use
```

The most common variant. Port 80 or 443 is occupied by a system web server or another container.

### Secondary port binding failure

```
Error starting userland proxy: listen tcp4 0.0.0.0:3306: bind: address already in use
```

A database port like 3306 or 5432 is already bound by a locally installed database server.

### Compose multi-service conflict

```
ERROR: for api_1  Cannot start service api:
Ports are not available: port is already allocated
ERROR: for worker_1  Cannot start service worker:
Ports are not available: port is already allocated
```

Multiple services in the same compose file fail because they all try to bind the same host port.

### Orphaned container binding

```
Error response from daemon: Bind for 0.0.0.0:8080 failed:
port is already allocated
```

A container that was not properly removed during the last `docker compose down` still holds the port.

## How to Fix It

### Solution 1: Find and stop the conflicting process

Identify exactly what is using the port and stop it.

```bash
# Find process using port 8080
sudo lsof -i :8080
sudo netstat -tlnp | grep :8080
sudo ss -tlnp | grep :8080

# Kill the process if safe to do so
sudo kill $(sudo lsof -t -i :8080)
```

If the conflict is another Docker container:

```bash
# List all containers and their port bindings
docker ps --format "table {{.Names}}\t{{.Ports}}\t{{.Status}}"

# Stop the specific container
docker stop <container_name>
```

### Solution 2: Clean up orphaned containers

Previous compose runs may have left containers running in the background.

```bash
# Stop all compose services and remove orphans
docker compose down --remove-orphans

# Nuclear option: stop all containers
docker stop $(docker ps -q)

# Remove all stopped containers
docker container prune -f

# Verify ports are free
docker ps --format "table {{.Names}}\t{{.Ports}}"
```

### Solution 3: Remap host ports to avoid conflicts

Change the host port in the compose file to an unused port.

```yaml
services:
  web:
    ports:
      - "8080:80"    # Changed from "80:80"
      - "8443:443"   # Changed from "443:443"
  db:
    ports:
      - "54330:5432" # Changed from "5432:5432"
```

Use environment variables for flexible port configuration:

```yaml
services:
  web:
    ports:
      - "${WEB_PORT:-8080}:80"
  db:
    ports:
      - "${DB_PORT:-54330}:5432"
```

```bash
# Set custom ports via .env file
echo "WEB_PORT=9090" >> .env
echo "DB_PORT=54331" >> .env
```

### Solution 4: Use dynamic port assignment

Let Docker pick available ports automatically.

```yaml
services:
  web:
    ports:
      - "80"    # Only container port, Docker picks host port
```

Find the assigned port after starting:

```bash
docker compose up -d
docker compose port web 80
# Output: 0.0.0.0:49153
```

### Solution 5: Use network_mode host (Linux only)

Bypass port mapping entirely by using the host network directly.

```yaml
services:
  web:
    network_mode: host
```

This eliminates port conflicts with other containers but limits you to one instance per host.

## Common Scenarios

### Running multiple compose projects simultaneously

Two different projects bind the same port because they use identical port mappings.

```yaml
# Project A - docker-compose.yml
services:
  web:
    ports:
      - "3000:3000"

# Project B - docker-compose.yml
services:
  web:
    ports:
      - "3000:3000"  # CONFLICT
```

Fix by using different ports per project or separate networks:

```yaml
# Project B - docker-compose.yml
services:
  web:
    ports:
      - "3001:3000"  # Different host port
```

### System service conflicting with Docker

PostgreSQL, Nginx, or Redis installed on the host occupies the same port Docker needs.

```bash
# Check if PostgreSQL is running on the host
sudo systemctl status postgresql

# Option A: Stop the host service
sudo systemctl stop postgresql

# Option B: Change the Docker port mapping
# In docker-compose.yml
# ports: "5433:5432" instead of "5432:5432"
```

### Rapid development restart cycles

During development, repeatedly running `docker compose down && docker compose up` causes timing issues where ports are not released fast enough.

```bash
# Add a delay between down and up
docker compose down
sleep 2
docker compose up -d

# Or use --wait flag
docker compose down --timeout 10
docker compose up -d
```

## Prevent It

- **Use environment variables for port configuration**: Never hardcode host ports in compose files. Define them in `.env` files so each developer and environment can use different ports without modifying the compose file.
- **Always use `--remove-orphans` when tearing down**: Make it a habit to run `docker compose down --remove-orphans` instead of just `docker compose down`. This prevents orphaned containers from silently holding port bindings.
- **Add a port availability check to startup scripts**: Before running `docker compose up`, add a preflight script that checks whether the required host ports are available and warns about conflicts before Docker reports them.
