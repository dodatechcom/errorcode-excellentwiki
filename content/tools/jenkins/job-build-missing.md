---
title: "[Solution] Jenkins Job/Build Permission Missing"
description: "Fix Jenkins Job/Build permission missing errors. Resolve build trigger permission issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Job/Build Permission Missing

The `Job/Build` permission is required to trigger builds.

## How to Fix

```bash
# Manage Jenkins > Configure Security > Authorization
# Matrix: add user/group > Job/Build
```

Minimum permissions: Overall/Read, Job/Read, Job/Build, Job/Workspace
