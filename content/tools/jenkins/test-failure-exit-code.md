---
title: "[Solution] Test Failure Exit Code in Jenkins Build"
description: "Fix test failure exit codes in Jenkins builds. Resolve failing tests and build abort issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Test Failure Exit Code in Jenkins Build

Test failures cause the build to fail with a non-zero exit code.

## Common Causes

- Legitimate test failures
- Flaky tests
- Test environment issues
- Test timeout exceeded

## How to Fix

```groovy
stage('Test') {
    steps {
        catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
            sh 'mvn test -B'
        }
    }
}
```

```groovy
post { always { junit '**/surefire-reports/*.xml' } }
```
