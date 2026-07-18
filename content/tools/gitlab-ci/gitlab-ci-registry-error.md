---
title: "[Solution] GitLab CI Registry Error"
description: "Fix GitLab CI registry errors. Learn why this happens and how to resolve it quickly."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# GitLab CI Registry Error

Registry errors occur when GitLab Container Registry push, pull, or auth operations fail.

## Why This Happens

- Token lacks registry access
- Image too large
- Registry quota exceeded
- Docker login failed

## Common Error Messages

- `registry_push_failed`
- `registry_pull_failed`
- `registry_auth_error`
- `registry_quota_error`

## How to Fix It

### Solution 1: Use CI job token

Authenticate with CI job variables:

```bash
docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
```

### Solution 2: Optimize image size

Use multi-stage builds to reduce image size:

```dockerfile
FROM node:18 AS builder
RUN npm ci
FROM node:18-slim
COPY --from=builder /app/node_modules ./node_modules
```

### Solution 3: Manage registry quota

Set up cleanup policies in Settings > CI/CD > Container Registry.


## Common Scenarios

- **Unauthorized on push:** Verify the token has write access to the registry.
- **Registry quota exceeded:** Delete old images or set up automatic cleanup.

## Prevent It

- Use CI_REGISTRY_*
- Implement cleanup
- Use multi-stage builds
