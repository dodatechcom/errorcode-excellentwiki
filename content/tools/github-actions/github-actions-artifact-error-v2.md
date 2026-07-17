---
title: "GitHub Actions Artifact Upload Failed"
description: "GitHub Actions artifact action fails to upload or download artifacts."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# GitHub Actions — Artifact Upload Failed

This error occurs when the `actions/upload-artifact` action fails to upload an artifact. The artifact may be too large, the path may be incorrect, or the workflow may lack permissions.

## Common Causes

- Artifact path does not exist
- Artifact size exceeds limit
- Multiple artifacts with the same name
- Workflow permissions insufficient
- Disk space issue on runner

## How to Fix

### Verify Artifact Path Exists

```yaml
- run: ls -la dist/
- uses: actions/upload-artifact@v4
  with:
    name: build-output
    path: dist/
```

### Set Artifact Name Uniquely

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: build-${{ github.run_number }}
    path: dist/
```

### Configure Artifact Retention

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: coverage-report
    path: coverage/
    retention-days: 7
```

### Check Artifact Size

```bash
du -sh dist/
```

### Download Artifact in Another Job

```yaml
- uses: actions/download-artifact@v4
  with:
    name: build-output
    path: dist/
```

## Examples

```text
Error: Artifact with name 'build-output' already exists for this workflow run.
```

## Related Errors

- [GitHub Actions Cache Error]({{< relref "/tools/github-actions/github-actions-cache-error" >}}) — cache restore failure
- [GitHub Actions Permission Error]({{< relref "/tools/github-actions/github-actions-permission-error" >}}) — permission issues
- [GitHub Actions Runner Error]({{< relref "/tools/github-actions/github-actions-runner-error" >}}) — runner issues
