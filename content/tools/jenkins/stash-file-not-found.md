---
title: "[Solution] Jenkins Stash File Not Found"
description: "Fix Jenkins stash file not found errors. Resolve stash/unstash file transfer issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Stash File Not Found

Stash/unstash transfers files between nodes.

## How to Fix

```groovy
node('agent-a') {
    stash includes: 'build/**/*', name: 'my-build'
}
node('agent-b') {
    unstash 'my-build'
    archiveArtifacts artifacts: 'build/**/*'
}
```
