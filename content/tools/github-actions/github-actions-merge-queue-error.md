---
title: "[Solution] GitHub Actions Merge Queue Error"
description: "Fix GitHub Actions merge queue configuration errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Merge queue errors occur when the merge queue is not properly configured:

```
Error: Merge queue is not enabled for this repository
```

## Common Causes

- Merge queue not enabled in repository settings.
- Workflow does not support merge queue events.

## How to Fix

**Add merge_group event to workflow:**

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  merge_group:
```

## Examples

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  merge_group:
    types: [checks-requested]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
```
