---
title: "[Solution] Jenkins Signup Disabled Error"
description: "Fix Jenkins signup disabled errors. Resolve user registration and self-signup issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Signup Disabled Error

Jenkins disables user self-registration by default.

## How to Fix

```bash
java -jar jenkins-cli.jar -s http://localhost:8080/ create-user --password mypass --email user@example.com newuser
```
