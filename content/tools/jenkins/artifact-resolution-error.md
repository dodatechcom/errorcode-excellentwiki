---
title: "[Solution] Jenkins Artifact Resolution Error"
description: "Fix Jenkins artifact resolution errors. Resolve cross-build artifact dependency issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Artifact Resolution Error

Artifact resolution errors occur when Jenkins cannot find artifacts from a previous build.

## How to Fix

```groovy
copyArtifacts(projectName: 'upstream-job', filter: 'target/*.jar', selector: lastCompleted())
```

```groovy
buildDiscarder(logRotator(numToKeepStr: '50', artifactNumToKeepStr: '20'))
```
