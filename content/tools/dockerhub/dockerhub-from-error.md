---
title: "[Solution] DockerHub FROM Error"
description: "Fix DockerHub FROM instruction errors. Resolve base image specification issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub FROM Error can prevent your application from working correctly.

## Common Causes

- FROM syntax error
- Image not specified
- AS name invalid

## How to Fix

### Correct FROM

```dockerfile
FROM node:18-alpine
```

