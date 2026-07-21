---
title: "[Solution] DockerHub Repository Not Found"
description: "Fix DockerHub repository not found errors. Resolve repository lookup issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Repository Not Found can prevent your application from working correctly.

## Common Causes

- Repository does not exist
- Wrong repository name
- Private repo access denied
- Organization namespace wrong

## How to Fix

### Check Repository

```bash
docker search my-repo
```

### Verify Name

```bash
docker pull username/repo:tag
```

