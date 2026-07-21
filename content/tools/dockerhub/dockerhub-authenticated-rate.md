---
title: "[Solution] DockerHub Authenticated Rate Error"
description: "Fix DockerHub authenticated rate errors. Resolve authenticated pull limits."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Authenticated Rate Error can prevent your application from working correctly.

## Common Causes

- Authenticated limit: 200 per 6 hours
- Rate exceeded

## How to Fix

### Check Usage

```bash
curl -s -I "https://hub.docker.com/v2/repositories/library/nginx" | grep -i ratelimit
```

