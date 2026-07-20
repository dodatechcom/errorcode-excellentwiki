---
title: "[Solution] GitHub Actions Repository Not Found Error"
description: "Fix GitHub Actions repository not found errors during checkout."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Repository not found errors occur when trying to access a repository that does not exist or is inaccessible:

```
Error: fatal: repository 'https://github.com/org/missing-repo.git/' not found
```

## Common Causes

- Repository name is incorrect.
- Repository was deleted or renamed.
- Repository is private and token lacks access.

## How to Fix

**Verify the repository exists:**

```bash
gh repo view {owner}/{repo} --json name,visibility
```

**Ensure token has repo access:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      repository: owner/repo
      token: ${{ secrets.CROSS_REPO_TOKEN }}
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      repository: owner/repo
```
