---
title: "[Solution] Jenkins Token Authentication Failed"
description: "Fix Jenkins token authentication failures. Resolve API token and credential authentication issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Token Authentication Failed

Token authentication failures occur when Jenkins rejects the API token.

## How to Fix

```bash
# Jenkins > User > Configure > API Token > Generate New Token
curl -u username:new-api-token http://jenkins:8080/api/json
```
