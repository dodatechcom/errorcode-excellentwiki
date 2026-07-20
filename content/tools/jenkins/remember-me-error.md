---
title: "[Solution] Jenkins Remember Me Error"
description: "Fix Jenkins remember me login errors. Resolve persistent login and session issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Remember Me Error

Remember me allows users to stay logged in. Errors occur when sessions expire.

## How to Fix

```bash
# Manage Jenkins > Configure System > Jenkins URL
# https://jenkins.example.com/
```

Check reverse proxy cookie forwarding.
