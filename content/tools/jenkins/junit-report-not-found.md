---
title: "[Solution] JUnit Report Not Found in Jenkins Build"
description: "Fix JUnit report not found errors in Jenkins. Resolve test report archiving and display issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# JUnit Report Not Found in Jenkins Build

The `junit` step fails when no test result XML files match the specified pattern.

## Common Causes

- Test step did not run
- Report path pattern is wrong
- Build was aborted before tests completed

## How to Fix

```groovy
post {
    always {
        junit allowEmptyResults: true, testResults: '**/surefire-reports/*.xml'
    }
}
```

### Common Test Report Locations

```groovy
junit '**/surefire-reports/*.xml'    // Maven
junit '**/build/test-results/**/*.xml' // Gradle
junit 'test-results/*.xml'            // Jest
```
