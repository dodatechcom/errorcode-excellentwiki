---
title: "[Solution] Docker Stats Error — no running containers"
description: "Fix Docker stats 'no running containers' error. Monitor container resource usage and start stopped containers."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "docker"
tags: ["docker", "containers", "stats", "monitoring", "containers"]
severity: "error"
weight: 5
---

# ERROR: no running containers

## Error Message

```
Error: no running containers

Error: StatService: unable to retrieve stats: no running containers found
```

This error occurs when `docker stats` is invoked but no containers are currently in a running state. The stats command can only display metrics for active containers.

## Common Causes

- All containers have exited or been stopped
- Containers were removed with `docker rm` instead of just stopped
- Docker Compose services have not been started yet
- The Docker daemon is not running and no container state is available
- Filters in the stats command exclude all running containers

## Solutions

### Solution 1: Start Your Containers

Before running stats, ensure at least one container is running. Use `docker compose up` or `docker start` depending on your setup.

```bash
docker compose up -d
docker stats
```

### Solution 2: List All Containers to Find Stopped Ones

Check what containers exist and which are stopped. Start the ones you want to monitor.

```bash
docker ps -a
docker start myapp db redis
docker stats
```

### Solution 3: Use Stats with Specific Container Names

If you have many containers, target specific ones by name. This avoids the error when only certain containers need monitoring.

```bash
docker stats myapp db
```

### Solution 4: Monitor Stats with CSV Output

For automated monitoring pipelines, use `--no-stream` with `--format` to capture a single snapshot. This avoids streaming timeout issues when containers stop mid-capture.

```bash
docker stats --no-stream --format "table {{.Name}}	{{.CPUPerc}}	{{.MemUsage}}"
```

## Prevention Tips

- Use `--restart unless-stopped` on containers you want to monitor continuously
- Set up Docker health checks to detect and auto-restart failed containers
- Use `docker events` to monitor container state changes in real time
- Combine `docker stats` with Prometheus and cAdvisor for long-term metrics

## Related Errors

- [Container Not Running]({{< relref "/tools/docker/container-is-not-running" >}}) — container must be running
- [Container Exited]({{< relref "/tools/docker/container-exited" >}}) — container exit code errors
