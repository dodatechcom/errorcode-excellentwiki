---
title: "[Solution] Jenkins Copy Artifact from Upstream Error"
description: "Fix Jenkins copy artifact from upstream errors. Resolve cross-build artifact copying issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Copy Artifact from Upstream Error

Copy artifact errors occur when the Copy Artifact plugin cannot retrieve artifacts.

## How to Fix

```bash
# Manage Jenkins > Plugins > Available > Install "Copy Artifact"
```

```groovy
copyArtifacts(projectName: 'my-upstream-job', selector: lastSuccessful(), filter: 'target/*.jar')
```
