---
title: "[Solution] Docker Secrets — permission denied"
description: "Fix Docker secrets permission denied errors. Resolve secret access issues in Docker Swarm and build contexts."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["secrets", "permission-denied", "swarm", "build", "credentials"]
weight: 5
---

# Docker Secrets — permission denied

Docker secrets permission denied errors occur when containers or build processes cannot access configured secrets. Secrets have strict access controls and specific mount behaviors.

## Common Causes

- Container not granted access to the secret
- Secret not created or has a different name
- Secret mount path is read-only (by design) and app tries to write
- Build-time secrets not properly configured with BuildKit

## How to Fix

### Grant Secret Access in Service

```bash
docker service create \
  --name my-app \
  --secret db_password \
  my-app:latest
```

### Reference Secret in Compose

```yaml
version: '3.8'
services:
  web:
    image: my-app:latest
    secrets:
      - db_password
    environment:
      - DB_PASS_FILE=/run/secrets/db_password

secrets:
  db_password:
    file: ./secrets/db_password.txt
```

### Use BuildKit Secrets

```dockerfile
# syntax=docker/dockerfile:1
FROM node:20-alpine
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc \
    npm install
```

```bash
docker build --secret id=npmrc,src=.npmrc .
```

### Check Secret Permissions

```bash
docker secret ls
docker secret inspect <secret-name>
```

## Examples

```bash
# Example 1: Secret not accessible in container
docker exec my-app cat /run/secrets/db_password
# cat: /run/secrets/db_password: Permission denied
# Fix: ensure --secret flag is passed to the service

# Example 2: Build-time secret missing
docker build --secret id=npmrc,src=.npmrc .
# ERROR: failed to solve: mounted source does not exist
# Fix: verify file exists: ls -la .npmrc

# Example 3: Swarm secret not created
docker service create --secret db_pass my-app
# Error: secret db_pass not found
# Fix: echo "mypassword" | docker secret create db_pass -
```

## Related Errors

- [Docker Socket Error]({{< relref "/tools/docker/docker-socket" >}}) — cannot connect to Docker daemon
- [Permission Denied]({{< relref "/tools/docker/permission-denied3" >}}) — general Docker permission issues
- [Docker BuildKit Error]({{< relref "/tools/docker/docker-buildkit" >}}) — build failed with secrets
