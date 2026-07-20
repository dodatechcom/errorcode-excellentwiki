---
title: "[Solution] Jenkins Bitbucket Integration Error"
description: "Fix Jenkins Bitbucket integration errors. Resolve Bitbucket webhook and SCM connection issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Bitbucket Integration Error

Bitbucket integration errors occur when Jenkins cannot properly connect to Bitbucket for SCM operations or receive webhooks.

## Common Causes

- Bitbucket plugin not installed or misconfigured
- Webhook URL not accessible from Bitbucket
- Credentials mismatch

## How to Fix

```bash
# Manage Jenkins > Plugins > Available > Install "Bitbucket"
```

```groovy
pipeline {
    agent any
    triggers { bitbucketPush() }
    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: 'main']],
                    userRemoteConfigs: [[url: 'https://bitbucket.org/myorg/myrepo.git', credentialsId: 'bitbucket-app-password']]
                ])
            }
        }
    }
}
```
