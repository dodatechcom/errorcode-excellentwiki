---
title: "[Solution] Jenkins Inject Passwords Error"
description: "Fix Jenkins inject passwords step errors. Resolve password injection and credential binding failures."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Inject Passwords Error

The `injectPasswords` step fails when it cannot inject the specified credentials.

## How to Fix

```bash
# Manage Jenkins > Plugins > Available > Install "Credentials Binding"
```

```groovy
withCredentials([
    string(credentialsId: 'api-key', variable: 'API_KEY'),
    usernamePassword(credentialsId: 'db-creds', usernameVariable: 'DB_USER', passwordVariable: 'DB_PASS'),
    file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')
]) {
    sh "echo \$API_KEY"
}
```
