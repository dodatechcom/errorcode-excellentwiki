---
title: "[Solution] DockerHub Base Image Error"
description: "Fix DockerHub base image errors. Resolve base image issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Base Image Error can prevent your application from working correctly.

## Common Causes

- Base image not found
- Base image deprecated
- Base image insecure

## How to Fix

### Use Official Images

```dockerfile
FROM ubuntu:22.04
FROM node:18-alpine
```

