---
title: "[Solution] DockerHub Anonymous Rate Error"
description: "Fix DockerHub anonymous rate errors. Resolve unauthenticated pull limits."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Anonymous Rate Error can prevent your application from working correctly.

## Common Causes

- Anonymous pull limit: 100 per 6 hours
- IP-based limiting

## How to Fix

### Authenticate

```bash
docker login
```

