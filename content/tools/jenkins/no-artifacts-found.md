---
title: "[Solution] No Artifacts Found in Jenkins Build"
description: "Fix no artifacts found errors in Jenkins. Resolve artifact generation and archiving issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# No Artifacts Found in Jenkins Build

No artifacts found means the build did not produce any matching files.

## How to Fix

```groovy
sh 'ls -la target/'
archiveArtifacts artifacts: 'target/*.jar', allowEmptyArchive: true, fingerprint: true
```
