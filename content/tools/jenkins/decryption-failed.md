---
title: "[Solution] Jenkins Credential Decryption Failed"
description: "Fix Jenkins credential decryption failures. Resolve encrypted credential access and key issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Credential Decryption Failed

Decryption failures occur when Jenkins cannot decrypt stored credentials.

## Common Causes

- Master key changed
- Credentials copied from different instance
- `credentials.xml` is corrupted

## How to Fix

```bash
ls -la $JENKINS_HOME/credentials.xml
# Delete and re-add credentials through Jenkins UI
```
