---
title: "[Solution] Jenkins Username Password Credentials Not Found"
description: "Fix Jenkins username/password credential lookup errors. Resolve credential binding failures."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Username Password Credentials Not Found

The `usernamePassword` credential binding fails when the credential ID does not exist or is wrong type.

## How to Fix

```groovy
withCredentials([usernamePassword(credentialsId: 'github-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
    sh 'echo "User: $USERNAME"'
}
```
