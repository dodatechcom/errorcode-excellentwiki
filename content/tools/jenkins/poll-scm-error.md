---
title: "[Solution] Jenkins Poll SCM Configuration Error"
description: "Fix Jenkins Poll SCM configuration errors. Resolve SCM polling schedule and trigger issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Poll SCM Configuration Error

Poll SCM configuration errors prevent Jenkins from checking for changes.

## How to Fix

```groovy
pipeline {
    agent any
    triggers { pollSCM('H/5 * * * *') }
    stages {
        stage('Checkout') { steps { checkout scm } }
    }
}
```

### Use Webhook Instead

```groovy
pipeline { triggers { githubPush() } ... }
```
