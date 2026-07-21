---
title: "[Solution] DockerHub Image Pull Denied"
description: "Fix DockerHub image pull denied errors. Resolve pull permission issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Image Pull Denied can prevent your application from working correctly.

## Common Causes

- Not authenticated
- Private repo access denied
- Rate limited

## How to Fix

### Login

```bash
docker login
```

### Check Access

```bash
docker pull username/repo:tag
```

