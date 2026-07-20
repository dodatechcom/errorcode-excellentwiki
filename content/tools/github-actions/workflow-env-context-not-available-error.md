---
title: "[Solution] Workflow Env Context Not Available Error"
description: "Fix GitHub Actions env context not available errors in workflow expressions."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The `env` context is not available in certain parts of the workflow file:

```
Error: env context is not available here
```

## Common Causes

- Using `${{ env.VARIABLE }}` in the `on` trigger (env is only available in steps).
- Referencing `env` at the workflow level before any step sets it.
- Using `env` in `jobs.<job_id>.runs-on`.

## How to Fix

**Env is available in steps, not in on trigger:**

```yaml
env:
  NODE_VERSION: 20

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Use Node.js
        run: node --version
        # env.VARIABLE is available here
```

## Examples

```yaml
# Wrong - env not available in on trigger
on:
  push:
    branches: [main]
env:
  MY_VAR: hello
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo ${{ env.MY_VAR }}  # OK in steps
```
