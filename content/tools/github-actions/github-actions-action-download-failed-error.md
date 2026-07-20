---
title: "[Solution] GitHub Actions Action Download Failed Error"
description: "Fix GitHub Actions action download failed errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Action download failures occur when GitHub Actions cannot download the referenced action:

```
Error: Failed to download action 'actions/checkout@v4'
Error: connect ECONNREFUSED 140.82.121.4:443
```

## Common Causes

- Network connectivity issues.
- GitHub API rate limit exceeded.
- Action repository is private without proper auth.

## How to Fix

**Use a specific SHA for reliability:**

```yaml
- uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11
```

**Check action availability:**

```bash
gh api repos/actions/checkout/releases/latest | jq '.tag_name'
```

## Examples

```yaml
- uses: actions/checkout@v4
  with:
    fetch-depth: 0
```
