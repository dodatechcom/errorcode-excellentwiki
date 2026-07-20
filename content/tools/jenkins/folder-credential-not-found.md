---
title: "[Solution] Jenkins Folder Credential Not Found"
description: "Fix Jenkins folder-scoped credential not found errors. Resolve credential scope and access issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Folder Credential Not Found

Folder-scoped credentials are only accessible within the folder where they are defined.

## How to Fix

```groovy
withCredentials([string(credentialsId: 'my-folder/my-cred', variable: 'TOKEN')]) {
    sh 'echo $TOKEN'
}
```
