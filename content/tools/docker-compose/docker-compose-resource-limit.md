---
title: "[Solution] Docker Compose Resource Limit Exceeded Error — How to Fix"
description: "Fix Docker Compose memory or CPU limit exceeded errors. Resolve OOM kills, resource constraints, and container throttling issues now."
comments: true
---

## What This Error Means

The `resource limit exceeded` error occurs when a container exceeds the memory or CPU limits defined in the Docker Compose configuration. The Docker daemon kills the container with an OOM (Out of Memory) error or throttles CPU usage beyond the allocated amount.

A typical error:

```
ERROR: for web  Cannot start service web:
OCI runtime create failed: container_linux.go:380:
starting container process caused: process_linux.go:545:
container init caused: rootfs_linux.go:76: mounting
"/sys/fs/cgroup" caused: no space left on device
```

Or:

```
container terminated with exit code 137 (OOM killed)
```

Or:

```
docker: Error response from daemon: OCI runtime create
failed: unable to start container process:
exec: "java": resource temporarily unavailable
```

Or:

```
Memory limit exceeded: Kill process 12345 (java)
score 500 or sacrifice child
```

## Why It Happens

Resource limit errors occur when:

- **Memory limit too low**: The application requires more RAM than the container limit allows.
- **Java/JVM heap exceeds container limit**: JVM defaults to using a large heap that may exceed the Docker memory limit.
- **No memory limit set**: Without limits, a runaway process consumes all host memory, triggering the OOM killer.
- **CPU starvation**: Too many containers compete for limited CPU resources, causing throttling.
- **Disk I/O contention**: High disk usage combined with memory pressure causes cascading failures.
- **Memory leaks**: The application gradually consumes more memory until it hits the limit.
- **Swap disabled**: Containers cannot use swap memory, so any excess immediately triggers OOM.

## Common Error Messages

### OOM killed container

```
container terminated with exit code 137 (OOM killed)
```

Exit code 137 means the process was killed by the OOM killer (128 + signal 9 = SIGKILL).

### cgroup memory limit exceeded

```
memory: usage 524288000, limit 524288000, failcnt 1234
memory+swap: usage 524288000, limit 1048576000
```

The container used all allocated memory and was terminated.

### CPU throttling

```
throttled_time: 5.32s
nr_periods: 1000
nr_throttled: 200
```

The container was throttled for 200 out of 1000 scheduling periods due to CPU limits.

### Resource temporarily unavailable

```
Error: unable to start container process:
exec: "python": resource temporarily unavailable
```

The system cannot fork new processes because all available memory is consumed.

## How to Fix It

### Solution 1: Increase memory limits

Set appropriate memory limits based on application requirements.

```yaml
services:
  api:
    image: myapi:latest
    deploy:
      resources:
        limits:
          memory: 1G
          cpus: "2.0"
        reservations:
          memory: 512M
          cpus: "1.0"
    environment:
      - JAVA_OPTS=-Xms256m -Xmx768m
```

Check current resource usage:

```bash
# Monitor container resource usage
docker stats --no-stream

# Check specific container
docker stats myapp_api --no-stream

# View detailed container inspect
docker inspect myapp_api --format '{{.HostConfig.Memory}}'
```

### Solution 2: Set JVM heap size for Java applications

Java applications often default to using 1/4 of host memory, ignoring container limits.

```yaml
services:
  api:
    image: myjavaapp:latest
    environment:
      # Set explicit heap size
      - JAVA_OPTS=-Xms256m -Xmx512m
      # Or use container-aware settings (JDK 10+)
      - JAVA_OPTS=-XX:+UseContainerSupport -XX:MaxRAMPercentage=75.0
    deploy:
      resources:
        limits:
          memory: 1G
```

```dockerfile
# Dockerfile - use entrypoint that respects JAVA_OPTS
ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS -jar app.jar"]
```

### Solution 3: Configure memory and CPU limits properly

Use both limits and reservations for predictable resource allocation.

```yaml
services:
  web:
    image: nginx:latest
    # Compose V2 syntax (no deploy key)
    mem_limit: 512m
    cpus: 1.5
    mem_reservation: 256m

  api:
    image: myapi:latest
    # Compose V3 syntax (with deploy key)
    deploy:
      resources:
        limits:
          memory: 2G
          cpus: "4.0"
        reservations:
          memory: 1G
          cpus: "2.0"
```

### Solution 4: Monitor and auto-restart on OOM

Configure automatic restarts when containers are killed by OOM.

```yaml
services:
  api:
    image: myapi:latest
    restart: on-failure:5
    deploy:
      resources:
        limits:
          memory: 1G
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 10s
      timeout: 5s
      retries: 3
```

Monitor OOM events:

```bash
# Check if containers were OOM killed
docker inspect myapp_api --format '{{.State.OOMKilled}}'

# View container exit history
docker inspect myapp_api --format '{{json .State}}' | jq .

# Check system logs for OOM events
dmesg | grep -i "oom\|killed"
journalctl -k | grep -i "oom\|killed"
```

### Solution 5: Profile application memory usage

Measure actual memory needs before setting limits.

```bash
# Run without limits first to measure usage
docker run -d --name test myapi:latest

# Monitor memory over time
docker stats test --format "table {{.Container}}\t{{.MemUsage}}\t{{.MemPerc}}"

# Set limit to 1.5x the observed peak usage
docker stats test --format "{{.MemPerc}}" | sort -rn | head -1
```

### Solution 6: Use cgroup v2 for better resource control

Modern Linux systems use cgroup v2 which provides more accurate resource accounting.

```bash
# Check cgroup version
cat /proc/filesystems | grep cgroup

# Docker info shows cgroup version
docker info | grep -i cgroup

# Mount cgroup v2 if needed
sudo mount -t cgroup2 none /sys/fs/cgroup
```

## Common Scenarios

### Java application OOM in container

Java applications allocate heap memory based on available system memory, not container limits.

```yaml
services:
  api:
    image: openjdk:17-alpine
    command: java -jar app.jar
    mem_limit: 512m
    environment:
      # WRONG - JVM ignores container limit
      # - JAVA_OPTS=

      # CORRECT - explicitly limit heap
      - JAVA_OPTS=-Xms128m -Xmx384m -XX:+UseContainerSupport
```

### Node.js memory limit

Node.js has a default heap limit of about 1.5GB. In containers with lower memory limits, this can cause OOM.

```yaml
services:
  api:
    image: node:18-alpine
    command: node --max-old-space-size=384 server.js
    mem_limit: 512m
    environment:
      - NODE_OPTIONS=--max-old-space-size=384
```

### Multiple containers exceeding host memory

Running too many containers with high memory limits on a single host.

```bash
# Check total memory allocated vs available
docker stats --no-stream --format "table {{.Name}}\t{{.MemUsage}}" | \
  awk '{sum += $3} END {print "Total allocated:", sum}'

# Check host memory
free -h

# Identify the most memory-hungry containers
docker stats --no-stream --format "table {{.Name}}\t{{.MemPerc}}" | \
  sort -k2 -rn | head -5
```

```yaml
# Stagger resource-intensive services
services:
  api:
    mem_limit: 1G
  worker:
    mem_limit: 512M
  scheduler:
    mem_limit: 256M
```

## Prevent It

- **Always set memory limits**: Never deploy to production without explicit memory limits. Without them, a single misbehaving container can consume all host memory and crash every other service. Set limits based on profiling the application under realistic load.
- **Profile before setting limits**: Run the application without limits first and monitor its actual memory usage under typical and peak load. Set the limit to 1.5x the observed peak to provide headroom for traffic spikes and garbage collection.
- **Enable container-aware JVM settings**: For Java applications, always use `-XX:+UseContainerSupport` (JDK 10+) and `-XX:MaxRAMPercentage` instead of fixed `-Xmx` values. This lets the JVM respect container memory limits and adjust heap size dynamically.
