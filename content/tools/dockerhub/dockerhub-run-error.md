---
title: "[Solution] DockerHub RUN Error"
description: "Fix DockerHub RUN instruction errors. Resolve command execution issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub RUN Error can prevent your application from working correctly.

## Common Causes

- Command failed
- Package not found
- Permission denied

## How to Fix

### Fix RUN

```dockerfile
RUN apt-get update && apt-get install -y package
```

