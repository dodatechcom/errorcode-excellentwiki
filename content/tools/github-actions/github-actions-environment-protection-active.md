---
title: "[Solution] GitHub Actions Environment Protection Active"
description: "Fix GitHub Actions environment protection rules blocking deployments."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Environment protection rules can block deployments when not satisfied:

```
Error: Deployment blocked by environment protection rules
```

## Common Causes

- Required reviewers not configured or not approved.
- Wait timer not elapsed.
- Restricted to certain branches only.

## How to Fix

**Check environment settings:**

```bash
gh api repos/{owner}/{repo}/environments/production
```

## Examples

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://example.com
    steps:
      - uses: actions/checkout@v4
```
