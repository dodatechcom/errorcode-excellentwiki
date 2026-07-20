---
title: "[Solution] GitHub Actions Required Reviewers Not Approved"
description: "Fix GitHub Actions required reviewers approval errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Required reviewers not approved errors block deployment:

```
Error: Waiting for required reviewers to approve deployment
```

## Common Causes

- No reviewers have approved the deployment.
- Reviewers are unavailable.

## How to Fix

**Wait for manual approval:**

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4
```

## Examples

```yaml
jobs:
  deploy:
    environment:
      name: production
```
