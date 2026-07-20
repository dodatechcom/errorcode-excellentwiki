---
title: "[Solution] Jenkins Access Denied for User"
description: "Fix Jenkins access denied errors for specific users. Resolve user authentication and authorization issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Access Denied for User

Access denied errors occur when a user is authenticated but not authorized.

## How to Fix

```groovy
import hudson.model.User
def user = User.get('username')
println user?.hasPermission(hudson.model.Hudson.READ)
```

```bash
# Manage Jenkins > Configure Security > Authorization > Add user with permissions
```
