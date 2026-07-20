---
title: "[Solution] Jenkins Job Name Invalid"
description: "Fix Jenkins invalid job name errors. Resolve job naming convention and character issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Job Name Invalid

Job names must follow specific naming rules.

## Valid Characters

Letters, numbers, hyphens, underscores. No spaces, slashes, colons.

```
my-project    valid
my_project    valid
My Project    invalid (spaces)
my/project    invalid (slash)
```
