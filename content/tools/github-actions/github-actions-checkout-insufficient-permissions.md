---
title: "[Solution] GitHub Actions Checkout Insufficient Permissions"
description: "Fix GitHub Actions checkout insufficient permissions errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Insufficient permissions errors occur when the token cannot access the repository:

```
Error: Permission denied to repository
fatal: unable to access: The requested URL returned error: 403
```

## Common Causes

- Repository permissions are restricted.
- `GITHUB_TOKEN` lacks required scopes.

## How to Fix

**Set required permissions in workflow:**

```yaml
permissions:
  contents: read
  packages: read

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
  issues: write
  pull-requests: write
```
