---
title: "[Solution] DockerHub Build Argument Error"
description: "Fix DockerHub build argument errors. Resolve ARG instruction issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Build Argument Error can prevent your application from working correctly.

## Common Causes

- ARG not declared
- ARG value not provided
- ARG scope incorrect

## How to Fix

### Use Build Args

```dockerfile
ARG NODE_VERSION=18
FROM node:${NODE_VERSION}
```

