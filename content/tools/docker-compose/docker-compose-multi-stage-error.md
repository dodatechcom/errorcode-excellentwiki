---
title: "[Solution] Docker Compose Multi-Stage Build Target Error — How to Fix"
description: "Fix Docker Compose multi-stage build target not found errors. Resolve missing build stages, stage naming issues, and target resolution failures."
comments: true
---

## What This Error Means

The `multi-stage build target not found` error occurs when Docker Compose or BuildKit references a build stage name that does not exist in the Dockerfile. Multi-stage Dockerfiles define multiple named stages, and the target must match exactly.

A typical error:

```
ERROR: failed to solve: failed to resolve dockerfile
stage "production": dockerfile has no stage named "production"
```

Or:

```
target: build: not found
failed to solve: failed to resolve dockerfile
stage "build": failed to resolve stage "build"
```

Or:

```
FROM stage not found: failed to find image with name
"build" in dockerfile
```

Or:

```
multiple stages found but no target specified:
use --target to specify a build stage
```

## Why It Happens

Multi-stage build target errors occur when:

- **Stage name typo**: The `target:` value in the compose file does not exactly match a stage name in the Dockerfile.
- **Case sensitivity**: Docker stage names are case-sensitive. `Production` and `production` are different stages.
- **Stage was renamed or removed**: The Dockerfile was updated and a stage was renamed but the compose file still references the old name.
- **No stages defined**: The Dockerfile is a single-stage file but the compose file specifies a target.
- **Include directive issues**: Using Dockerfile includes or syntax that creates stages dynamically.
- **Target specified for wrong service**: The `target:` is set on a service that uses a different Dockerfile than expected.

## Common Error Messages

### Stage name not found

```
ERROR: failed to solve: failed to resolve dockerfile
stage "builder": dockerfile has no stage named "builder"
```

The compose file references a stage called `builder` but the Dockerfile does not define it.

### No target specified with multiple stages

```
multiple stages found but no target specified
```

The Dockerfile has multiple stages but the compose file does not specify which one to build.

### Target in wrong Dockerfile

```
ERROR: failed to solve: failed to resolve dockerfile
stage "production": 
open Dockerfile.prod: no such file or directory
```

The compose file specifies a target but the referenced Dockerfile does not contain that stage.

### FROM reference to non-existent stage

```
FROM builder AS final
ERROR: stage "builder" not found
```

A Dockerfile stage uses `FROM` to reference another stage that does not exist.

## How to Fix It

### Solution 1: Verify stage names in the Dockerfile

List all defined stages to confirm the correct name.

```bash
# Show all stage names from a Dockerfile
grep -n '^FROM' Dockerfile

# Example output:
# 1: FROM node:18-alpine AS build
# 15: FROM node:18-alpine AS production
# 23: FROM nginx:alpine AS serve
```

```yaml
# compose file - match the exact stage name
services:
  web:
    build:
      context: .
      target: production   # Must match FROM ... AS production
```

### Solution 2: Fix capitalization and spelling

Docker stage names are case-sensitive. Ensure exact matching.

```dockerfile
# Dockerfile
FROM node:18-alpine AS Build      # Capital B
FROM node:18-alpine AS Production # Capital P
```

```yaml
# WRONG - lowercase does not match
services:
  web:
    build:
      target: build       # Dockerfile has "Build" (capital B)

# CORRECT - exact match required
services:
  web:
    build:
      target: Build
```

### Solution 3: Remove target for single-stage Dockerfiles

If the Dockerfile has only one stage, remove the target directive.

```dockerfile
# Single-stage Dockerfile - no AS clause
FROM node:18-alpine
WORKDIR /app
COPY . .
RUN npm install
CMD ["node", "server.js"]
```

```yaml
# WRONG - specifying target on single-stage Dockerfile
services:
  web:
    build:
      context: .
      target: production    # This stage does not exist

# CORRECT - no target needed
services:
  web:
    build:
      context: .
```

### Solution 4: Add target to specify which stage to build

When the Dockerfile has multiple stages, always specify the target.

```dockerfile
# Dockerfile with multiple stages
FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:18-alpine AS production
WORKDIR /app
COPY --from=build /app/dist ./dist
COPY --from=build /app/package*.json ./
RUN npm ci --production
CMD ["node", "dist/server.js"]
```

```yaml
# Build only the production stage
services:
  web:
    build:
      context: .
      target: production
```

### Solution 5: Debug with docker build directly

Bypass Compose to test the build and identify the exact error.

```bash
# Test build with explicit target
docker build --target production -t myapp:latest .

# Test without target (builds last stage)
docker build -t myapp:latest .

# List stages and their digests
docker build --target build -t myapp:build-stage .
docker build --target production -t myapp:prod-stage .
docker image inspect myapp:build-stage --format '{{.Id}}'
docker image inspect myapp:prod-stage --format '{{.Id}}'
```

## Common Scenarios

### Different targets for dev and production

The compose file should build different stages depending on the environment.

```dockerfile
# Dockerfile
FROM node:18-alpine AS base
WORKDIR /app
COPY package*.json ./

FROM base AS development
RUN npm install
COPY . .
CMD ["npm", "run", "dev"]

FROM base AS build
RUN npm ci
COPY . .
RUN npm run build

FROM node:18-alpine AS production
WORKDIR /app
COPY --from=build /app/dist ./dist
COPY --from=build /app/node_modules ./node_modules
CMD ["node", "dist/server.js"]
```

```yaml
# docker-compose.yml (development)
services:
  web:
    build:
      context: .
      target: development

# docker-compose.prod.yml (production)
services:
  web:
    build:
      context: .
      target: production
```

### Renamed stage breaks compose

A developer renames a Dockerfile stage without updating the compose file.

```bash
# BEFORE
# Dockerfile: FROM node:18-alpine AS builder

# AFTER - renamed to "build"
# Dockerfile: FROM node:18-alpine AS build
```

```yaml
# compose file still references old name
services:
  web:
    build:
      target: builder    # BROKEN - renamed to "build"
```

Fix by updating the compose file:

```yaml
services:
  web:
    build:
      target: build      # Updated to match renamed stage
```

### Using build args with stage targets

Build arguments can dynamically determine which stage to build.

```yaml
services:
  web:
    build:
      context: .
      target: ${BUILD_TARGET:-development}
      args:
        - NODE_ENV=production
```

```bash
# Build development target
docker compose build

# Build production target
BUILD_TARGET=production docker compose build
```

## Prevent It

- **Document stage names in a comment at the top of the Dockerfile**: Add a comment listing all available stages and their purposes. This makes it easy for developers to know valid target values without reading the entire file.
- **Use CI validation to catch target mismatches**: Add a CI step that extracts stage names from the Dockerfile and verifies that all `target:` values in compose files match. This catches mismatches before they reach production.
- **Keep Dockerfile and compose file in the same PR**: When renaming or removing a Dockerfile stage, always update the corresponding compose file in the same commit. Separate changes create windows where the compose file references a non-existent target.
