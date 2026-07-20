---
title: "[Solution] GitHub Actions Runner OOM Killed Error"
description: "Fix GitHub Actions runner out of memory killed errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Runner OOM killed errors occur when the runner process or job runs out of memory:

```
Error: The runner has received a shutdown signal. This can happen
when the runner is running out of memory.
```

## Common Causes

- Job requires more memory than the runner has available.
- Memory leak in the build or test process.
- Running too many parallel jobs on a small runner.

## How to Fix

**Limit parallel jobs on self-hosted runner:**

```bash
./config.sh --concurrent 1
```

**Reduce memory usage in workflow:**

```yaml
steps:
  - name: Build with limited memory
    run: NODE_OPTIONS="--max-old-space-size=2048" npm run build
```

## Examples

```yaml
# Use larger runner
runs-on: ubuntu-latest-4-cores

# Limit Node.js memory
env:
  NODE_OPTIONS: "--max-old-space-size=4096"
```
