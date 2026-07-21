---
title: "[Solution] DockerHub Manifest Unknown Error"
description: "Fix DockerHub manifest unknown errors. Resolve manifest lookup issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Manifest Unknown Error can prevent your application from working correctly.

## Common Causes

- Manifest not found
- Tag does not exist

## How to Fix

### Check Manifest

```bash
docker manifest inspect username/repo:tag
```

