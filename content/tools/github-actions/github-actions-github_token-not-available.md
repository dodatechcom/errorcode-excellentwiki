---
title: "[Solution] GitHub Actions GITHUB_TOKEN Not Available"
description: "Fix GitHub Actions GITHUB_TOKEN not available errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

GITHUB_TOKEN not available errors occur when the default token is missing or restricted:

```
Error: HttpError: Not Found
Resource not accessible by integration
```

## Common Causes

- Token does not have sufficient permissions for the operation.
- Workflow does not have `permissions` configured.

## How to Fix

**Set explicit permissions:**

```yaml
permissions:
  contents: read
  issues: write
  pull-requests: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
```

## Examples

```yaml
permissions:
  contents: read
  packages: write
  issues: write
```
