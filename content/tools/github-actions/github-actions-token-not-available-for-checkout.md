---
title: "[Solution] GitHub Actions Token Not Available For Checkout"
description: "Fix GitHub Actions token not available errors during repository checkout."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Token errors occur when checkout requires authentication but the token is missing:

```
Error: fatal: unable to access 'https://github.com/private-org/repo.git/':
The requested URL returned error: 403
```

## Common Causes

- Default `GITHUB_TOKEN` does not have sufficient permissions.
- Checking out a different private repository.

## How to Fix

**Use a PAT or GitHub App token for cross-repo checkout:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      repository: private-org/private-repo
      token: ${{ secrets.PAT_TOKEN }}
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      token: ${{ secrets.PAT_TOKEN }}
      fetch-depth: 0
```
