---
title: "GitHub Actions Runner Offline Error"
description: "GitHub Actions runner is offline or not available to execute the workflow."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["github-actions", "runner", "offline", "self-hosted", "agent"]
weight: 5
---

# GitHub Actions — Runner Offline Error

This error occurs when a GitHub Actions runner is offline or not available to execute the workflow. Self-hosted runners may lose connectivity or be shut down.

## Common Causes

- Self-hosted runner machine is powered off
- Runner lost network connectivity
- Runner service crashed or stopped
- Runner is overwhelmed with jobs
- Organization removed runner access

## How to Fix

### Check Runner Status

Go to **Settings > Actions > Runners** to see the runner's status.

### Restart Runner Service

```bash
# Linux
sudo ./svc.sh restart

# Windows
.\svc.sh restart
```

### Use GitHub-Hosted Runners

```yaml
jobs:
  build:
    runs-on: ubuntu-latest  # GitHub-hosted
```

### Configure Runner Auto-Start

```bash
# Configure runner as a service
sudo ./svc.sh install
sudo ./svc.sh start
```

### Set Runner Labels

```yaml
jobs:
  build:
    runs-on: [self-hosted, linux, x64]
```

### Monitor Runner Health

```bash
# Check runner logs
tail -f ./_diag/Roller_*.log
```

## Examples

```text
Error: The runner 'my-runner' received a shutdown signal.
This is a runner request error, not an Actions error.
```

## Related Errors

- [GitHub Actions Timeout Error]({{< relref "/tools/github-actions/github-actions-timeout-error" >}}) — job timeout
- [GitHub Actions Runner Error]({{< relref "/tools/github-actions/github-actions-runner-error" >}}) — runner configuration issues
- [GitHub Actions Matrix Error]({{< relref "/tools/github-actions/github-actions-matrix-error" >}}) — matrix strategy issues
