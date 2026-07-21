---
title: "[Solution] DockerHub Tag Already Exists"
description: "Fix DockerHub tag already exists errors. Resolve tag immutability issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Tag Already Exists can prevent your application from working correctly.

## Common Causes

- Tag cannot be overwritten
- Tag immutable on paid plan
- Tag already pushed

## How to Fix

### Use New Tag

```bash
docker tag my-image:latest my-image:v2
```

