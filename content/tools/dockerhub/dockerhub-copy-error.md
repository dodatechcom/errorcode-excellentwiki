---
title: "[Solution] DockerHub COPY Error"
description: "Fix DockerHub COPY instruction errors. Resolve file copy issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub COPY Error can prevent your application from working correctly.

## Common Causes

- Source file not found
- Destination path invalid
- Permission denied

## How to Fix

### Correct COPY

```dockerfile
COPY package.json ./
COPY --chown=node:node . .
```

