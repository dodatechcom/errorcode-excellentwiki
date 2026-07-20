---
title: "[Solution] Jenkins Secret Text Not Found"
description: "Fix Jenkins secret text credential not found errors. Resolve secret text binding failures."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Secret Text Not Found

The `string` credential binding for secret text fails when the credential ID does not exist.

## How to Fix

```bash
# Manage Jenkins > Credentials > System > Global credentials
# Kind: Secret text
```

```groovy
withCredentials([string(credentialsId: 'my-secret-text', variable: 'TOKEN')]) {
    sh 'curl -H "Authorization: Bearer $TOKEN" https://api.example.com'
}
```
