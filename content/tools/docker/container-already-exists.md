---
title: "[Solution] Docker Container Already Exists — container name already in use"
description: "Fix Docker container already exists error. Remove or rename conflicting containers."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# container name "/my-container" is already in use

This error occurs when you try to create a container with a name that is already assigned to another container (even a stopped one). Docker container names must be unique.

## Common Causes

- Previous container with same name not removed
- Previous container stopped but not deleted
- Docker Compose reusing old container names
- Manual `docker run` conflicting with compose containers

## How to Fix

### List Containers (Including Stopped)

```bash
docker ps -a --filter name=my-container
```

### Remove Existing Container

```bash
docker rm my-container
```

### Force Remove Running Container

```bash
docker rm -f my-container
```

### Use Different Name

```bash
docker run --name my-container-v2 my-image
```

### Use Random Name

```bash
docker run --rm my-image
```

## Examples

```bash
# Example 1: Remove stopped container
docker ps -a --filter name=web
# CONTAINER ID   IMAGE   STATUS
# abc123         nginx   Exited (0) 5 minutes ago

docker rm web
docker run --name web nginx

# Example 2: Force remove and recreate
docker rm -f web
docker run --name web nginx

# Example 3: Use timestamp name
docker run --name web-$(date +%s) nginx
```

## Related Errors

- [Container exited with code]({{< relref "/tools/docker/container-exited" >}}) — related error
- [Docker rm force]({{< relref "/tools/docker/docker-rm-force" >}}) — related error
