---
title: "[Solution] Jenkins Archive on Master Only Error"
description: "Fix Jenkins archive on master only errors. Resolve artifact archiving restrictions."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Archive on Master Only Error

The `archiveArtifacts` step only works on the master node by default.

## How to Fix

```groovy
node('remote-agent') {
    sh 'mvn package -B'
    stash includes: 'target/*.jar', name: 'artifacts'
}
node('master') {
    unstash 'artifacts'
    archiveArtifacts artifacts: 'target/*.jar'
}
```
