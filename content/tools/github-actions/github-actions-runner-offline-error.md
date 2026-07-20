---
title: "[Solution] GitHub Actions Runner Offline Error"
description: "Fix GitHub Actions runner offline errors when the runner is not responding."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Runner offline errors occur when a registered runner is not connected:

```
Error: The self-hosted runner is offline. Workflow run was cancelled.
```

## Common Causes

- Runner machine is powered off.
- Runner process crashed or was stopped.
- Network connectivity issues between runner and GitHub.

## How to Fix

**Start the runner manually:**

```bash
cd /actions-runner
./run.sh
```

**Run as a service:**

```bash
sudo ./svc.sh install
sudo ./svc.sh start
```

**Check runner status:**

```bash
gh api repos/{owner}/{repo}/actions/runners --jq '.runners[] | {name: .name, status: .status}'
```

## Examples

```bash
# Check runner process
ps aux | grep Runner.Listener

# Restart runner service
sudo ./svc.sh stop
sudo ./svc.sh start
```
