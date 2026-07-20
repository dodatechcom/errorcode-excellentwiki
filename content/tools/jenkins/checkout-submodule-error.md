---
title: "[Solution] Jenkins Git Submodule Checkout Error"
description: "Fix Git submodule checkout errors in Jenkins pipeline. Resolve submodule initialization and update failures."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Git Submodule Checkout Error

Git submodule errors occur when Jenkins fails to initialize or update submodules during checkout.

## Common Causes

- `.gitmodules` references wrong URLs
- Submodule repository is private
- Submodule commit does not exist

## How to Fix

```groovy
checkout([
    $class: 'GitSCM',
    branches: [[name: 'main']],
    userRemoteConfigs: [[url: env.GIT_URL]],
    extensions: [
        [$class: 'SubmoduleOption', disableSubmodules: false, recursiveSubmodules: true]
    ]
])
```
