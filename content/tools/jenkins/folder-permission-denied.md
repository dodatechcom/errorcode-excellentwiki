---
title: "[Solution] Jenkins Folder Permission Denied"
description: "Fix Jenkins folder permission denied errors. Resolve folder-level access control issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Folder Permission Denied

Folder permissions control access to jobs within folders.

## How to Fix

```bash
# Navigate to folder > Configure > Permissions
# Or use Role Strategy Plugin for folder-level roles
```

```groovy
withCredentials([string(credentialsId: 'my-folder/my-secret', variable: 'SECRET')]) {
    sh 'echo $SECRET'
}
```
