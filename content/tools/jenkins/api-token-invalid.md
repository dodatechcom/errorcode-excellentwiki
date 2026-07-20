---
title: "[Solution] Jenkins API Token Invalid"
description: "Fix Jenkins API token invalid errors. Resolve API token authentication failures."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins API Token Invalid

API tokens allow programmatic access to Jenkins.

## How to Fix

```bash
# Jenkins > User > Configure > API Token > Generate New Token
curl -u admin:abc123def456 http://jenkins:8080/api/json
```
