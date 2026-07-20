---
title: "[Solution] Expected 'steps' Block in Jenkins Stage"
description: "Fix 'expected steps' parsing error in Jenkins pipeline stages. Resolve missing steps blocks in Jenkinsfile."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Expected 'steps' Block in Jenkins Stage

The `expected 'steps'` error occurs when a declarative pipeline `stage` block does not contain a valid `steps` section.

## Common Causes

- Stage block contains directives (e.g., `when`, `agent`) but no `steps` block
- Misplaced `sh`, `echo`, or other step calls outside of a `steps` block

## How to Fix

```groovy
stage('Build') {
    steps {
        sh 'make'
    }
}
```

A stage with ONLY parallel does not need steps:

```groovy
stage('Tests') {
    parallel {
        stage('Unit') { steps { sh 'make test-unit' } }
        stage('Integration') { steps { sh 'make test-integration' } }
    }
}
```
