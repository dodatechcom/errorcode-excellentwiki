---
title: "[Solution] Jenkins Overall/Read Permission Missing"
description: "Fix Jenkins Overall/Read permission errors. Resolve global read permission issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Overall/Read Permission Missing

The `Overall/Read` permission is required to access most Jenkins pages.

## How to Fix

```bash
# Manage Jenkins > Configure Security > Authorization
# Matrix: add user/group > Overall/Read
```
