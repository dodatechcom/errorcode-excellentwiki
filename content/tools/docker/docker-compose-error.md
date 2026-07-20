---
title: "[Solution] Docker Compose Error — No containers found for project"
description: "Fix Docker Compose 'No containers found for project' error. Resolve compose service startup issues."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "docker"
tags: ["docker", "containers", "docker-compose", "containers", "orchestration"]
severity: "error"
weight: 6
---

# ERROR: No containers found for project

## Error Message

```
ERROR: No containers found for project myapp

The Compose file './docker-compose.yml' is valid, but no containers were created.

Run 'docker compose up' to start the services.
```

This error occurs when Docker Compose cannot find or start any containers for your project. It typically means the services defined in your Compose file never reached a running state.

## Common Causes

- The Compose file has syntax errors that prevent service creation
- Required images cannot be pulled due to network or registry issues
- Port conflicts prevent services from binding to their host ports
- Volume mount paths do not exist on the host machine
- The project name conflicts with an existing stopped project

## Solutions

### Solution 1: Validate Your Compose File

Run a syntax check on your Compose file before starting services. This catches YAML formatting issues and invalid configuration keys that silently prevent container creation.

```bash
docker compose config
```

### Solution 2: Remove Stale Containers and Recreate

Older containers from a previous run can block new ones from starting. Remove stopped containers and volumes, then bring the stack back up.

```bash
docker compose down --remove-orphans
docker compose up -d
```

### Solution 3: Check for Port Conflicts

Another process may already be using the ports your Compose file maps. Identify the conflicting process and stop it, or change the host port mapping.

```bash
docker compose ps
sudo lsof -i :8080
# Change port in docker-compose.yml: "8081:80"
docker compose up -d
```

### Solution 4: Build Images Before Starting

If your Compose file references a local build context, building explicitly gives you detailed error output for failed builds.

```bash
docker compose build
docker compose up -d
```

## Prevention Tips

- Always run `docker compose config` to validate before `docker compose up`
- Use `docker compose down --remove-orphans` when tearing down stacks
- Pin image versions in your Compose file to avoid unexpected pull failures
- Keep port mappings documented to avoid conflicts across projects

## Related Errors

- [Docker Port Conflict]({{< relref "/tools/docker/port-conflict" >}}) — port is already allocated
- [Docker Build Error]({{< relref "/tools/docker/layer-cache" >}}) — build cache issues
