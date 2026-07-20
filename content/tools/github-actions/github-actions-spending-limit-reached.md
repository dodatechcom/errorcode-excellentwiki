---
title: "[Solution] GitHub Actions Spending Limit Reached"
description: "Fix GitHub Actions spending limit reached errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Spending limit errors occur when the billing spending limit is hit:

```
Error: GitHub Actions: spending limit reached
```

## Common Causes

- Organization spending limit set too low.
- Unexpected surge in workflow runs.

## How to Fix

**Check and adjust spending limit:**

Go to Settings > Billing > Spending limit

## Examples

```yaml
- run: |
    gh api github.com/repos/{owner}/{repo}/actions/workflows       --jq '.workflows[] | {name: .name, state: .state}'
```
