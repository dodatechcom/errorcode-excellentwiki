---
title: "[Solution] Docker Compose OOM Error — Fix Memory Limit Exceeded / Killed"
description: "Fix Docker Compose OOM errors when containers exceed memory limits and are killed. Set memory reservations, optimize application memory usage, and configure swap."
---

## What This Error Means

Docker Compose OOM errors occur when a container exceeds its memory limit and the kernel Out-Of-Memory (OOM) killer terminates the process. The container exits with code 137 or 139.

A typical error:

```
Container exited with code 137
```

Or from docker events:

```
container oom killed
```

## Why It Happens

OOM errors happen when:

- **Memory limit is too low**: The container's `mem_limit` is insufficient for the workload.
- **Memory leak**: The application has a memory leak that grows over time.
- **No memory limit set**: The container can use all host memory and gets killed when the host runs out.
- **Swap is disabled**: No swap space available when memory pressure increases.
- **Too many containers**: Total memory of all containers exceeds host capacity.
- **JVM or Node.js heap too large**: Runtime memory pools are not tuned for container limits.

## How to Fix It

**Step 1: Check container exit code**

```bash
docker ps -a --filter "status=exited"
docker logs <container>
# Exit code 137 = SIGKILL (OOM)
```

**Step 2: Increase memory limits**

```yaml
services:
  app:
    image: my-app
    mem_limit: 2g
    mem_reservation: 1g
```

**Step 3: Add swap space**

```yaml
services:
  app:
    image: my-app
    mem_limit: 2g
    memswap_limit: 3g
```

**Step 4: Set runtime memory limits**

For Java:

```yaml
services:
  app:
    image: my-app
    environment:
      - JAVA_OPTS=-Xmx512m -Xms256m
```

For Node.js:

```yaml
services:
  app:
    image: my-app
    environment:
      - NODE_OPTIONS=--max-old-space-size=512
```

**Step 5: Monitor memory usage**

```bash
docker stats <container>
docker compose top
```

**Step 6: Use memory reservations**

```yaml
services:
  app:
    image: my-app
    deploy:
      resources:
        limits:
          memory: 2G
        reservations:
          memory: 1G
```

## Common Mistakes

- **Setting mem_limit equal to memswap_limit**: This disables swap entirely, causing immediate OOM on memory pressure.
- **Not setting heap limits for JVM/Node.js**: These runtimes do not auto-detect container memory limits.
- **Running without any memory limits**: Containers can consume all host memory and cause system-wide OOM.
- **Ignoring docker stats output**: Monitor memory trends to set appropriate limits.

## Related Pages

- [Docker Compose Healthcheck Error](/tools/docker-compose/docker-compose-healthcheck-error/) -- Healthcheck failures
- [Docker Compose Restart Loop](/tools/docker-compose/docker-compose-restart-loop/) -- Container crash loops
- [Kubectl Pod Pending](/tools/kubectl/kubectl-pod-pending/) -- Pod scheduling issues
