---
title: "[Solution] DockerHub OCI Distribution Error"
description: "Fix DockerHub OCI distribution errors. Resolve OCI distribution spec issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub OCI Distribution Error can prevent your application from working correctly.

## Common Causes

- OCI distribution not supported
- Spec version mismatch

## How to Fix

### Check OCI Compliance

```bash
docker manifest inspect username/repo:tag
```

