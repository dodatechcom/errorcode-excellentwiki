---
title: "[Solution] GitHub Actions Self-Hosted Runner Not Found"
description: "Fix GitHub Actions self-hosted runner not found errors when the runner cannot be located."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Self-hosted runner not found errors occur when the workflow references a runner that is not registered:

```
Error: The self-hosted runner 'my-runner' is not available for this repository.
```

## Common Causes

- Runner was removed from the repository or organization.
- Runner label does not match any registered runner.
- Runner was registered to a different repository.

## How to Fix

**Check registered runners:**

```bash
gh api repos/{owner}/{repo}/actions/runners
```

**Re-register the runner:**

```bash
./config.sh --url https://github.com/{owner}/{repo} --token {REGISTRATION_TOKEN}
```

## Examples

```yaml
# Wrong - runner label does not match
runs-on: my-custom-runner-v2

# Correct - use a label that exists
runs-on: self-hosted
```
