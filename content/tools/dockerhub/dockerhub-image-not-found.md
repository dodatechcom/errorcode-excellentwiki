---
title: "[Solution] DockerHub Image Not Found"
description: "Fix DockerHub image not found errors. Resolve image lookup issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Image Not Found can prevent your application from working correctly.

## Common Causes

- Image does not exist
- Wrong image name
- Tag does not exist

## How to Fix

### Search Image

```bash
docker search nginx
```

### Pull Image

```bash
docker pull nginx:latest
```

