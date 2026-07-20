---
title: "[Solution] GitHub Actions Third-Party Action Review"
description: "Fix GitHub Actions third-party action security review concerns."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Third-party action security review concerns require careful evaluation:

```
Warning: Using untrusted third-party action 'unknown-org/action@v1'
```

## Common Causes

- Action from unknown or untrusted source.
- Action has not been audited.
- Supply chain attack risk.

## How to Fix

**Pin to a specific commit SHA:**

```yaml
- uses: trusted-org/trusted-action@a1b2c3d4e5f6
```

**Use only verified creators:**

```yaml
# GitHub verified creators
- uses: actions/checkout@v4
- uses: actions/setup-node@v4
- uses: actions/upload-artifact@v4
```

**Review the action source:**

```bash
# Check the action repository
gh api repos/{owner}/{repo}/contents/action.yml
```

## Examples

```yaml
# Verified actions from GitHub
- uses: actions/checkout@v4
  with:
    fetch-depth: 0

# Pin to SHA for third-party
- uses: peaceiris/actions-gh-pages@068c335e4633200b3e176b5c14b4fefc074658c3
```
