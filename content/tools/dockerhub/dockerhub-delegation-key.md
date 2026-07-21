---
title: "[Solution] DockerHub Delegation Key Error"
description: "Fix DockerHub delegation key errors. Resolve delegation key management issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Delegation Key Error can prevent your application from working correctly.

## Common Causes

- Delegation key not found
- Key not added to repo

## How to Fix

### Add Delegation

```bash
docker trust signer add --key key.pem signer username/repo
```

