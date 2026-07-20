---
title: "[Solution] Jenkins Pipeline Input Step Timeout"
description: "Fix Jenkins pipeline input step timeout. Resolve manual approval and input waiting failures."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Pipeline Input Step Timeout

The `input` step pauses the pipeline and waits for human interaction. A timeout occurs when no one responds within the configured time limit.

## Common Causes

- No one available to approve the deployment
- Timeout value too short for the approval workflow
- Notification not reaching the right team

## How to Fix

```groovy
stage('Approval') {
    steps {
        input message: 'Deploy to production?', ok: 'Deploy', timeout: 30
    }
}
```

```groovy
timeout(time: 1, unit: 'HOURS') {
    input message: 'Approve deployment?', submitter: 'admin,lead-dev'
}
```
