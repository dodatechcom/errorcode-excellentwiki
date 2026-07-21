---
title: "[Solution] DockerHub Image Push Denied"
description: "Fix DockerHub image push denied errors. Resolve push permission issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Image Push Denied can prevent your application from working correctly.

## Common Causes

- Not authenticated
- Write access denied
- Namespace mismatch

## How to Fix

### Login

```bash
docker login
```

### Tag and Push

```bash
docker tag my-image username/repo:tag
docker push username/repo:tag
```

