---
title: "[Solution] Docker Multi-stage build error / stage not found"
description: "Fix Docker multi-stage build errors. Resolve stage not found, COPY --from issues, and stage reference problems."
tools: ["docker"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

# Docker Multi-stage build error / stage not found

Multi-stage builds allow copying artifacts between stages using `COPY --from`. Errors occur when referencing a stage that does not exist or has an incorrect name.

## Common Causes

- Stage name is misspelled in `COPY --from` instruction
- Stage number does not exist (referencing non-existent index)
- Stage was removed or renamed in a Dockerfile update
- AS alias not defined in the FROM instruction

## How to Fix

### Name Stages Explicitly

```dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json .
RUN npm install
COPY . .
RUN npm run build

FROM node:20-alpine AS runtime
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
CMD ["node", "dist/index.js"]
```

### Use Stage Index as Fallback

```dockerfile
# If you have: FROM node:20 AS builder
# Then: COPY --from=0 /app/dist ./dist  (index 0 = first FROM)
```

### Verify Stage Names

```bash
docker build --progress=plain -t my-app . 2>&1 | grep "COPY"
# Check the output for stage references
```

### List All Stages in Dockerfile

```bash
grep -n "^FROM" Dockerfile
# FROM node:20 AS builder    (stage 0)
# FROM alpine:3.18           (stage 1)
```

## Examples

```bash
# Example 1: Misspelled stage name
docker build .
# error: COPY failed: failed to fetch source digest: build target "bildr" not found
# Fix: COPY --from=builder (correct spelling)

# Example 2: Wrong stage index
docker build .
# error: COPY failed: invalid from flag value "10"
# Fix: check the actual stage index (0-based)

# Example 3: Stage not defined
docker build .
# error: COPY failed: from flag value "builder" is invalid
# Fix: ensure FROM ... AS builder exists in the Dockerfile
```

## Related Errors

- [Docker BuildKit Error]({{< relref "/tools/docker/docker-buildkit" >}}) — BuildKit failed to solve
- [Docker COPY Error]({{< relref "/tools/docker/docker-copy-error" >}}) — file not found in context
- [Build Failed]({{< relref "/tools/docker/build-failed2" >}}) — general build failures
