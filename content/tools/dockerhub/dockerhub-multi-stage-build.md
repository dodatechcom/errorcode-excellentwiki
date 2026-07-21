---
title: "[Solution] DockerHub Multi-Stage Build Error"
description: "Fix DockerHub multi-stage build errors. Resolve multi-stage compilation issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Multi-Stage Build Error can prevent your application from working correctly.

## Common Causes

- Stage not found
- Copy from stage failed
- Stage name wrong

## How to Fix

### Multi-Stage Build

```dockerfile
FROM node:18 AS builder
WORKDIR /app
COPY . .
RUN npm run build

FROM nginx
COPY --from=builder /app/dist /usr/share/nginx/html
```

