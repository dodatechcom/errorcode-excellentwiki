---
title: "[Solution] Jenkins Pipeline Parallel Step Failed"
description: "Fix Jenkins pipeline parallel step failures. Resolve parallel stage execution and error handling."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Pipeline Parallel Step Failed

Parallel steps in a Jenkins pipeline run concurrently within a single stage. When one or more parallel branches fail, the entire pipeline can fail.

## Common Causes

- One or more parallel branches encounter errors
- No error handling around parallel steps
- Resource contention between parallel branches

## How to Fix

### Use catchError for Non-Critical Branches

```groovy
stage('Tests') {
    parallel {
        stage('Unit Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE') {
                    sh 'make test-unit'
                }
            }
        }
        stage('Integration Tests') {
            steps {
                sh 'make test-integration'
            }
        }
    }
}
```

### Add Fail Fast Option

```groovy
stage('Tests') {
    failFast true
    parallel {
        stage('A') { steps { sh 'make test-a' } }
        stage('B') { steps { sh 'make test-b' } }
    }
}
```
