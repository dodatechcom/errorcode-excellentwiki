---
title: "[Solution] GitHub Actions Runner Not Compatible Error"
description: "Fix GitHub Actions runner not compatible errors due to version or OS mismatch."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Runner not compatible errors occur when the runner version or OS does not meet workflow requirements:

```
Error: Runner version 2.300.0 is not compatible with required version 2.310.0
```

## Common Causes

- Runner binary is outdated.
- Workflow requires features from a newer runner version.
- OS-specific actions running on incompatible runner OS.

## How to Fix

**Update the runner:**

```bash
cd /actions-runner
./config.sh remove
curl -O https://github.com/actions/runner/releases/download/v2.310.0/actions-runner-linux-x64-2.310.0.tar.gz
tar xzf actions-runner-linux-x64-2.310.0.tar.gz
./config.sh --url https://github.com/{owner}/{repo} --token {TOKEN}
```

## Examples

```yaml
runs-on: ubuntu-latest
```
