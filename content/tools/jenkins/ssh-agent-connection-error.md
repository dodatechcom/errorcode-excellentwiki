---
title: "[Solution] Jenkins SSH Agent Connection Error"
description: "Fix Jenkins SSH agent connection errors. Resolve SSH agent launcher and connectivity issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins SSH Agent Connection Error

SSH agent connection errors occur when Jenkins cannot SSH into a remote agent.

## How to Fix

```bash
ssh -o StrictHostKeyChecking=no user@agent-host "java -version"
ssh-keyscan agent.example.com >> ~/.ssh/known_hosts
```
