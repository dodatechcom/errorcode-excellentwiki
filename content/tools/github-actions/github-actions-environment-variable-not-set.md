---
title: "[Solution] GitHub Actions Environment Variable Not Set"
description: "Fix GitHub Actions environment variable not set errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Environment variable not set errors occur when the workflow references undefined env vars:

```
Error: $MY_VAR: unbound variable
```

## Common Causes

- Variable not defined in workflow, job, or step level.
- Variable set in wrong scope.
- Variable name typo.

## How to Fix

**Define env vars at the appropriate level:**

```yaml
env:
  GLOBAL_VAR: "value"

jobs:
  build:
    runs-on: ubuntu-latest
    env:
      JOB_VAR: "job-value"
    steps:
      - run: echo $GLOBAL_VAR $JOB_VAR
        env:
          STEP_VAR: "step-value"
```

## Examples

```yaml
env:
  NODE_ENV: production

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo $NODE_ENV
```
