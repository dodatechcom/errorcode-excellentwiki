---
title: "[Solution] Jenkins Label Expression No Match"
description: "Fix Jenkins label expression no match errors. Resolve agent label expression evaluation failures."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Label Expression No Match

Label expressions use boolean logic. When no agent satisfies the expression, the build waits.

## How to Fix

```groovy
agent { label 'linux && docker && gpu && fast' }  // complex
agent { label 'linux' }                            // simpler
agent { label 'fast-server || linux' }             // with fallback
```
