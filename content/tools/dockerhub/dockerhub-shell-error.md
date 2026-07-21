---
title: "[Solution] DockerHub SHELL Error"
description: "Fix DockerHub SHELL instruction errors. Resolve shell configuration issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub SHELL Error can prevent your application from working correctly.

## Common Causes

- Shell not found
- Shell syntax error

## How to Fix

### Correct SHELL

```dockerfile
SHELL ["/bin/bash", "-c"]
```

