---
title: "[Solution] DockerHub OCI Manifest Error"
description: "Fix DockerHub OCI manifest errors. Resolve OCI specification issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub OCI Manifest Error can prevent your application from working correctly.

## Common Causes

- OCI manifest invalid
- Manifest format wrong

## How to Fix

### Use OCI Format

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t username/repo:tag --push .
```

