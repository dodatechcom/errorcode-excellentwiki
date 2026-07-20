---
title: "[Solution] Jenkins Agent Label Not Found"
description: "Fix Jenkins agent label not found errors. Resolve label expression matching issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Agent Label Not Found

Jenkins uses labels to match builds to agents. When no agent matches, the build waits.

## Common Causes

- Label does not match any agent
- Agent offline
- Typo in label name

## How to Fix

```groovy
agent { label 'linux' }
agent { label 'linux && docker' }
agent { label 'linux || any' }
agent any
```
