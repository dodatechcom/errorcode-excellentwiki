---
title: "[Solution] DockerHub Multi-Arch Image Error"
description: "Fix DockerHub multi-arch image errors. Resolve multi-architecture build issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Multi-Arch Image Error can prevent your application from working correctly.

## Common Causes

- Architecture not supported
- Build failed for platform

## How to Fix

### Build Multi-Arch

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t username/repo:tag --push .
```

