---
title: "[Solution] Jenkins Domain Credential Missing"
description: "Fix Jenkins domain credential missing errors. Resolve domain-scoped credential configuration issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Domain Credential Missing

Jenkins organizes credentials into domains. When a credential is stored in a specific domain but referenced from a different domain, it cannot be found.

## How to Fix

```bash
# Manage Jenkins > Credentials > System > Global credentials
# Store credentials in the default (global) domain
```

```groovy
withCredentials([string(credentialsId: 'my-domain/credential-id', variable: 'SECRET')]) {
    sh 'echo $SECRET'
}
```
