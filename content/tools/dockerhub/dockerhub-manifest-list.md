---
title: "[Solution] DockerHub Manifest List Error"
description: "Fix DockerHub manifest list errors. Resolve multi-architecture manifest issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Manifest List Error can prevent your application from working correctly.

## Common Causes

- Manifest list not found
- Architecture not included

## How to Fix

### Create Manifest List

```bash
docker manifest create username/repo:tag username/repo:amd64 username/repo:arm64
```

