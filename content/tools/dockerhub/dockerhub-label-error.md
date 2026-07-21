---
title: "[Solution] DockerHub LABEL Error"
description: "Fix DockerHub LABEL instruction errors. Resolve metadata label issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub LABEL Error can prevent your application from working correctly.

## Common Causes

- Label syntax error
- Value too long

## How to Fix

### Correct LABEL

```dockerfile
LABEL maintainer="user@example.com"
```

