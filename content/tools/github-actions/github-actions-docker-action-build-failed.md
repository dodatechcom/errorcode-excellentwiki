---
title: "[Solution] GitHub Actions Docker Action Build Failed"
description: "Fix GitHub Actions Docker action build failures."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Docker action build failures occur when the Docker image cannot be built:

```
Error: failed to solve: rpc error: code = Unknown desc = error reading from server: EOF
```

## Common Causes

- Dockerfile has syntax errors.
- Base image not available.
- Build context too large.
- Network issues pulling base images.

## How to Fix

**Build the Docker image locally first:**

```bash
docker build -t my-action:latest .
```

**Use a simpler Dockerfile:**

```dockerfile
FROM node:20-slim
COPY . /action
WORKDIR /action
RUN npm install --production
ENTRYPOINT ["node", "/action/index.js"]
```

**Reference the Docker action in workflow:**

```yaml
steps:
  - uses: actions/checkout@v4
  - uses: ./.github/actions/my-docker-action
```

## Examples

```dockerfile
# Minimal Dockerfile for a GitHub Action
FROM node:20-slim
COPY package*.json ./
RUN npm ci --production
COPY . .
ENTRYPOINT ["node", "index.js"]
```
