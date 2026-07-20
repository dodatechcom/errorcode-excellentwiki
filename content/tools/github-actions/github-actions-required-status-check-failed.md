---
title: "[Solution] GitHub Actions Required Status Check Failed"
description: "Fix GitHub Actions required status check failures blocking merge."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Required status check failures prevent PR merging:

```
Error: 1 required status check is expected: build
```

## Common Causes

- CI workflow failed.
- Status check not triggered (e.g., wrong event type).

## How to Fix

**Ensure CI runs on pull_request:**

```yaml
on:
  pull_request:
    branches: [main]
```

## Examples

```yaml
on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
```
