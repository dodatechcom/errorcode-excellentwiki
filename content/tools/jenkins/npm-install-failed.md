---
title: "[Solution] NPM Install Failed in Jenkins Pipeline"
description: "Fix npm install failures in Jenkins pipeline. Resolve Node.js dependency installation issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# NPM Install Failed in Jenkins Pipeline

NPM install failures occur when `npm install` or `npm ci` cannot install dependencies.

## Common Causes

- npm registry unreachable or rate limited
- `package-lock.json` out of sync
- Native module compilation fails
- Disk space exhausted

## How to Fix

```groovy
pipeline {
    agent any
    tools { nodejs 'Node-18' }
    stages {
        stage('Install') { steps { sh 'npm ci --prefer-offline' } }
    }
}
```
