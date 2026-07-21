---
title: "[Solution] DockerHub Authentication Required"
description: "Fix DockerHub authentication required errors. Resolve login issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Authentication Required can prevent your application from working correctly.

## Common Causes

- Not logged in
- Credentials expired
- 2FA required

## How to Fix

### Login

```bash
docker login -u username
```

