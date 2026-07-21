---
title: "Docker Multi-Stage Build Error"
description: "Multi-stage Dockerfile build fails during stage transition"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Docker Multi-Stage Build Error

Multi-stage Dockerfile build fails during stage transition

## Common Causes

- COPY --from references non-existent build stage
- Stage name typo or missing FROM alias
- Build context does not contain required files
- Stage produces no output or empty image

## How to Fix

1. Check stage names: verify FROM ... AS <name> aliases match COPY --from
2. Use `docker build --target <stage>` to test individual stages
3. Check build logs: `docker build --progress=plain .`
4. Verify file paths in COPY/ADD instructions

## Examples

```dockerfile
# Example multi-stage build
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
```
