---
title: "[Solution] Jenkins Matrix Auth Permission Denied"
description: "Fix Jenkins matrix authorization permission denied errors. Resolve user and role permission issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Matrix Auth Permission Denied

Permission denied errors occur when matrix authorization does not grant required permissions.

## How to Fix

```bash
# Manage Jenkins > Configure Security > Authorization
# Add user/group with: Overall/Read, Job/Read, Job/Build, Job/Workspace
```

```groovy
def user = hudson.model.User.current()
println "Has Overall/Read: ${user?.hasPermission(hudson.model.Hudson.READ)}"
```
