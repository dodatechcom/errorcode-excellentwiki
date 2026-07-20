---
title: "[Solution] Jenkins Unstash Failed Error"
description: "Fix Jenkins unstash failed errors. Resolve file restoration issues from stash."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Unstash Failed Error

Unstash fails when Jenkins cannot restore files from a previous stash.

## How to Fix

```groovy
try {
    unstash 'my-artifacts'
} catch (err) {
    echo "Failed to unstash: ${err.message}"
    sh 'make build'
}
```
