---
title: "[Solution] DockerHub Pull Rate Limit Error"
description: "Fix DockerHub pull rate limit errors. Resolve image pull throttling."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Pull Rate Limit Error can prevent your application from working correctly.

## Common Causes

- Anonymous pull limit exceeded
- Authenticated pull limit hit

## How to Fix

### Login

```bash
docker login
```

### Use Mirror

Configure registry mirror for caching.

