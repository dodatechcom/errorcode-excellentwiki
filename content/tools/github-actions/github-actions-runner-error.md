---
title: "GitHub Actions Runner Error"
description: "GitHub Actions runner encounters an error during workflow execution."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["github-actions", "runner", "vm", "environment", "hosted"]
weight: 5
---

# GitHub Actions Runner Error

A GitHub Actions runner error occurs when the runner (virtual machine) encounters problems executing the workflow. This can be caused by environment issues, resource limits, or runner configuration problems.

## Common Causes

- Runner runs out of disk space
- Runner runs out of memory
- Software not available on the runner image
- Self-hosted runner configuration issues
- Docker permission issues

## How to Fix

### Check Disk Space

```yaml
- name: Check disk space
  run: df -h
```

### Free Up Disk Space

```yaml
- name: Free disk space
  uses: jlumbroso/free-disk-space@main
  with:
    tool-cache: false
    docker-images: true
    large-packages: true
```

### Use Larger Runner

```yaml
jobs:
  build:
    runs-on: ubuntu-latest-8-cores  # Larger runner with more resources
```

### Install Required Software

```yaml
- name: Install dependencies
  run: |
    sudo apt-get update
    sudo apt-get install -y build-essential
```

### Fix Self-Hosted Runner

```bash
# On the runner machine
./config.sh --url https://github.com/owner/repo --token TOKEN
./run.sh
```

### Check Runner Logs

```bash
# On self-hosted runner
cat _diag/*.log
```

## Examples

```yaml
# Error: disk space
Error: No space left on device

# Fix: free disk space
- uses: jlumbroso/free-disk-space@main
```

## Related Errors

- [Timeout Error]({{< relref "/tools/github-actions/github-actions-timeout-error" >}}) — job timeout
- [Workflow Error]({{< relref "/tools/github-actions/workflow-failed" >}}) — workflow failure
