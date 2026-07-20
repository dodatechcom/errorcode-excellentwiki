---
title: "[Solution] GitHub Actions No Runner Matching Labels Error"
description: "Fix GitHub Actions no runner matching labels errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

No runner matching labels errors occur when no registered runner has the requested labels:

```
Error: No runner matching the specified labels was found: gpu, cuda-12
```

## Common Causes

- Labels are too specific and no runner has them.
- Runner was removed but label is still in the workflow.
- Typo in label names.

## How to Fix

**Check available runner labels:**

```bash
gh api repos/{owner}/{repo}/actions/runners --jq '.runners[].labels[].name'
```

**Add labels to a runner:**

```bash
./config.sh --labels "gpu,cuda-12" --url https://github.com/{owner}/{repo} --token {TOKEN}
```

## Examples

```yaml
# Wrong - labels no runner has
runs-on: [self-hosted, gpu, cuda-12, arm64]

# Correct - labels runners actually have
runs-on: [self-hosted, linux, x64]
```
