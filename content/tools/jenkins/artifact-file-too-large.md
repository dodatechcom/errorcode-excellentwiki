---
title: "[Solution] Jenkins Artifact File Too Large"
description: "Fix Jenkins artifact file too large errors. Resolve artifact size limit and storage issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Artifact File Too Large

Artifact files that are too large consume excessive disk space.

## How to Fix

```groovy
archiveArtifacts artifacts: 'target/*.jar', excludes: '**/node_modules/**,**/target/classes/**'
```

```groovy
buildDiscarder(logRotator(numToKeepStr: '20', artifactNumToKeepStr: '5'))
```
