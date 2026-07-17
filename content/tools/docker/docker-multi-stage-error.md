---
title: "[Solution] Docker Multi-Stage Build Failed"
description: "Fix Docker multi-stage build failures. Resolve stage reference, COPY --from, and AS alias errors."
tools: ["docker"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A Docker multi-stage build error occurs when a Dockerfile references a build stage that does not exist, is misspelled, or has an incorrect index. Multi-stage builds allow copying artifacts between stages using `COPY --from`, and failures happen when stage names or indices are wrong.

## Common Causes

- Stage name is misspelled in `COPY --from` instruction
- Stage index does not exist (referencing non-existent index)
- Stage was removed or renamed in a Dockerfile update
- `AS` alias not defined in the `FROM` instruction
- Referencing a stage from a different build target

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
grep -n "^FROM" Dockerfile
# FROM node:20 AS builder    (stage 0)
# FROM alpine:3.18           (stage 1)
```

### Build with Debug Output

```bash
docker build --progress=plain -t my-app . 2>&1 | grep "COPY"
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

- [Docker BuildKit Error]({{< relref "/tools/docker/docker-buildkit-error" >}}) — BuildKit build error
- [Docker Compose Error]({{< relref "/tools/docker/docker-compose-error-v2" >}}) — docker compose up failed
- [Docker Volume Error]({{< relref "/tools/docker/docker-volume-error-v2" >}}) — volume mount permission denied
