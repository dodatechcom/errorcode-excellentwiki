---
title: "[Solution] Jenkins Agent Not Available"
description: "Fix Jenkins agent not available errors. Resolve agent allocation and scheduling failures."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Agent Not Available

The `agent not available` error means Jenkins cannot allocate an agent.

## Common Causes

- All matching agents offline or at capacity
- Label expression mismatch

## How to Fix

```groovy
pipeline { agent any ... }
```

```groovy
pipeline { agent { label 'linux || docker || any' } ... }
```
