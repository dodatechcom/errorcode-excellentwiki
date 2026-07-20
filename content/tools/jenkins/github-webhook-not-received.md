---
title: "[Solution] GitHub Webhook Not Received by Jenkins"
description: "Fix GitHub webhook not triggering Jenkins builds. Resolve webhook configuration and connectivity issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitHub Webhook Not Received by Jenkins

GitHub webhooks fail to trigger Jenkins builds when the webhook cannot reach the Jenkins server.

## Common Causes

- Jenkins URL not accessible from GitHub
- Webhook URL misconfigured
- Jenkins behind a reverse proxy without proper forwarding
- Webhook secret mismatch

## How to Fix

```groovy
pipeline {
    triggers { githubPush() }
    stages {
        stage('Build') {
            steps { checkout scm }
        }
    }
}
```

```bash
# GitHub > Repository > Settings > Webhooks > Add webhook
# Payload URL: https://jenkins.example.com/github-webhook/
```
