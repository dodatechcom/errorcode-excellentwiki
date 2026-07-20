---
title: "[Solution] Jenkins SCM Polling Failed"
description: "Fix Jenkins SCM polling failures. Resolve polling errors in Jenkinsfile and scheduled build triggers."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins SCM Polling Failed

SCM polling periodically checks the repository for changes. When polling fails, Jenkins cannot detect new commits.

## Common Causes

- Credentials for polling have expired
- Repository URL changed or unavailable
- Network connectivity issues

## How to Fix

```groovy
pipeline {
    triggers { pollSCM('H/5 * * * *') }
    stages {
        stage('Build') {
            steps { checkout scm }
        }
    }
}
```

### Switch to Webhook Triggering

```groovy
pipeline {
    triggers { githubPush() }
    stages { ... }
}
```
