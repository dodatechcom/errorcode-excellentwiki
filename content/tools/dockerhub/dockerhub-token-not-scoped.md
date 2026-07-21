---
title: "[Solution] DockerHub Token Not Scoped Error"
description: "Fix DockerHub token not scoped errors. Resolve token permission scope issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Token Not Scoped Error can prevent your application from working correctly.

## Common Causes

- Token lacks required scope
- Read-only token
- Token needs write access

## How to Fix

### Create Scoped Token

1. Go to Security > Access Tokens
2. Select appropriate scopes

