---
title: "[Solution] DockerHub HEALTHCHECK Error"
description: "Fix DockerHub HEALTHCHECK instruction errors. Resolve health check issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub HEALTHCHECK Error can prevent your application from working correctly.

## Common Causes

- Health check command failed
- Timeout too short
- Interval too long

## How to Fix

### Correct HEALTHCHECK

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost/ || exit 1
```

