---
title: "[Solution] Docker driver failed programming external connectivity"
description: "Fix 'driver failed programming external connectivity' error. Resolve Docker network port mapping failures on container startup."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker driver failed programming external connectivity

docker: Error response from daemon: driver failed programming external connectivity on endpoint <name>".

This error occurs when Docker cannot set up the network port mapping for a container. Typically caused by port conflicts or iptables issues.

## How to Fix

### Check Docker Status

```bash
docker info
docker system df
```

### View Logs

```bash
docker logs <container>
docker events --since 5m
```

### Restart Docker

```bash
sudo systemctl restart docker
```

## Related Errors

- [Container Not Running]({{< relref "/tools/docker/container-is-not-running" >}}) — container stopped
- [Image Not Found]({{< relref "/tools/docker/docker-image-not-found" >}}) — image missing
