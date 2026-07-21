---
title: "[Solution] DockerHub Scan Error"
description: "Fix DockerHub scan errors. Resolve image scanning failures."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Scan Error can prevent your application from working correctly.

## Common Causes

- Scan failed
- Scanner unavailable
- Image too large

## How to Fix

### Retry Scan

```bash
docker scan my-image
```

