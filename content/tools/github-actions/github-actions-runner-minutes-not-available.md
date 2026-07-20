---
title: "[Solution] GitHub Actions Runner Minutes Not Available"
description: "Fix GitHub Actions runner minutes not available errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Runner minutes not available errors occur when self-hosted runners have billing issues:

```
Error: No runners available for this workflow
```

## Common Causes

- Self-hosted runner machine is down.
- Runner group permissions changed.

## How to Fix

**Check runner availability:**

```bash
gh api repos/{owner}/{repo}/actions/runners --jq '.runners[] | {name: .name, status: .status}'
```

## Examples

```yaml
runs-on: ${{ github.repository_owner == 'myorg' && 'self-hosted' || 'ubuntu-latest' }}
```
