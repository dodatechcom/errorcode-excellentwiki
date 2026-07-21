---
title: "[Solution] DockerHub OS Not Supported Error"
description: "Fix DockerHub OS not supported errors. Resolve operating system compatibility issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub OS Not Supported Error can prevent your application from working correctly.

## Common Causes

- OS not supported
- Platform combination invalid

## How to Fix

### Check Supported OS

```bash
docker manifest inspect nginx | jq '.manifests[].platform.os'
```

