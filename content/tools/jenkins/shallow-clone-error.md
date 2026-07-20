---
title: "[Solution] Jenkins Shallow Clone Error"
description: "Fix shallow clone errors in Jenkins pipeline. Resolve depth-related checkout failures and missing commits."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Shallow Clone Error

Shallow clone errors occur when the clone depth is insufficient to reach the required commit.

## Common Causes

- Clone depth too shallow
- Force push moved commits beyond the shallow window
- Build requires a commit from earlier than the depth

## How to Fix

```groovy
extensions: [[$class: 'CloneOption', depth: 50]]
```

### Use Full Clone

```groovy
extensions: [[$class: 'CloneOption', depth: 0]]
```
