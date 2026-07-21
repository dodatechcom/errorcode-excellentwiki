---
title: "[Solution] DockerHub Image Manifest Error"
description: "Fix DockerHub image manifest errors. Resolve manifest format issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Image Manifest Error can prevent your application from working correctly.

## Common Causes

- Manifest invalid
- Manifest not found
- Schema version wrong

## How to Fix

### Check Manifest

```bash
docker manifest inspect username/repo:tag
```

