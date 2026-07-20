---
title: "[Solution] Archive Artifacts Not Found in Jenkins Build"
description: "Fix archive artifacts not found errors in Jenkins. Resolve missing artifact archiving issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Archive Artifacts Not Found in Jenkins Build

The `archiveArtifacts` step fails when the specified artifact patterns do not match any files.

## Common Causes

- Build step did not produce expected output
- Artifact pattern does not match actual paths
- Build failed before producing artifacts

## How to Fix

```groovy
archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
archiveArtifacts artifacts: 'dist/**/*', fingerprint: true
archiveArtifacts artifacts: 'build/reports/**/*', allowEmptyArchive: true
```
