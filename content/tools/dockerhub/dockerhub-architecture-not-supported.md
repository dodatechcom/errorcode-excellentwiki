---
title: "[Solution] DockerHub Architecture Not Supported Error"
description: "Fix DockerHub architecture not supported errors. Resolve platform compatibility issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Architecture Not Supported Error can prevent your application from working correctly.

## Common Causes

- Architecture not available
- Platform not supported

## How to Fix

### Check Available Platforms

```bash
docker manifest inspect nginx | jq '.manifests[].platform'
```

