---
title: "[Solution] DockerHub Content Trust Error"
description: "Fix DockerHub content trust errors. Resolve image signing and verification issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Content Trust Error can prevent your application from working correctly.

## Common Causes

- Content trust not enabled
- Signature verification failed

## How to Fix

### Enable Content Trust

```bash
export DOCKER_CONTENT_TRUST=1
```

