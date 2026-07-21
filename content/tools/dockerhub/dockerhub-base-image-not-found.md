---
title: "[Solution] DockerHub Base Image Not Found Error"
description: "Fix DockerHub base image not found errors. Resolve FROM instruction issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Base Image Not Found Error can prevent your application from working correctly.

## Common Causes

- Image does not exist
- Tag not found
- Registry not accessible

## How to Fix

### Check Image

```bash
docker pull ubuntu:22.04
```

