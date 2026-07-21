---
title: "[Solution] DockerHub ADD Error"
description: "Fix DockerHub ADD instruction errors. Resolve file addition issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub ADD Error can prevent your application from working correctly.

## Common Causes

- Source not found
- URL invalid
- Archive extraction failed

## How to Fix

### Use COPY Instead

```dockerfile
COPY file.txt ./
```

