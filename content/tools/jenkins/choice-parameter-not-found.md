---
title: "[Solution] Jenkins Choice Parameter Not Found"
description: "Fix Jenkins choice parameter not found errors. Resolve choice parameter definition and access issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Choice Parameter Not Found

Choice parameters provide a dropdown list of options.

## How to Fix

```groovy
parameters {
    choice(name: 'DEPLOY_ENV', choices: ['development', 'staging', 'production'])
}
```

```groovy
def env = params.DEPLOY_ENV
echo "Deploying to: ${env}"
```
