---
title: "[Solution] GitHub Actions Rate Limit Exceeded"
description: "Fix GitHub Actions API rate limit exceeded errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Rate limit errors occur when too many API calls are made:

```
Error: API rate limit exceeded for user
```

## Common Causes

- Too many GitHub API calls in the workflow.
- Using `gh` CLI excessively.

## How to Fix

**Check rate limit:**

```bash
gh api rate_limit | jq '.rate'
```

## Examples

```yaml
- run: |
    RATE=$(gh api rate_limit --jq '.rate.remaining')
    if [ "$RATE" -lt 10 ]; then
      echo "Rate limit low, skipping"
      exit 0
    fi
```
