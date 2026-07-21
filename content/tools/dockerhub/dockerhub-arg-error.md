---
title: "[Solution] DockerHub ARG Error"
description: "Fix DockerHub ARG instruction errors. Resolve build argument issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub ARG Error can prevent your application from working correctly.

## Common Causes

- ARG not available in runtime
- Default value wrong

## How to Fix

### Correct ARG

```dockerfile
ARG NODE_VERSION=18
FROM node:${NODE_VERSION}
```

