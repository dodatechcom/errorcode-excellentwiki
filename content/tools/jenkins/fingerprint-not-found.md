---
title: "[Solution] Jenkins Fingerprint Not Found"
description: "Fix Jenkins fingerprint not found errors. Resolve artifact fingerprint tracking issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Fingerprint Not Found

Fingerprints track artifact usage across builds.

## How to Fix

```groovy
archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
```

```bash
# Jenkins > Fingerprint
```
