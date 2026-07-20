---
title: "[Solution] Jenkins Anonymous Read Not Allowed"
description: "Fix Jenkins anonymous read access denied errors. Resolve anonymous user permission issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Anonymous Read Not Allowed

Anonymous read not allowed means anonymous users cannot view Jenkins pages.

## How to Fix

```bash
# Manage Jenkins > Configure Security > Authorization
# Matrix: anonymous > Overall/Read (check the box)
```
