---
title: "[Solution] GitHub Actions Step Failed"
description: "Fix GitHub Actions step failed errors. Resolve individual step failures in workflow jobs."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# GitHub Actions Step Failed

A step failed error means an individual step in a GitHub Actions job returned a non-zero exit code. The job stops unless `if: always()` or `continue-on-error` is set.

## Common Causes

- A shell command returned a non-zero exit code
- A `uses` action version is incorrect or the action failed
- A test assertion failed
- A script encountered a runtime error

## How to Fix

### Allow Steps to Continue on Error

```yaml
steps:
  - name: Run tests (non-blocking)
    run: npm test
    continue-on-error: true
```

### Use if: always() for Cleanup Steps

```yaml
steps:
  - name: Run tests
    run: npm test
  - name: Upload logs
    if: always()
    run: upload-logs.sh
```

### Debug the Failing Step

```yaml
# Enable debug logging
# Set Actions secret: ACTIONS_STEP_DEBUG = true
```

### Use Conditional Step Execution

```yaml
steps:
  - name: Deploy
    if: github.ref == 'refs/heads/main'
    run: deploy.sh
```

### Check Exit Code

```yaml
steps:
  - name: Run command
    id: run-cmd
    run: |
      ./my-script.sh
      echo "exit_code=$?" >> $GITHUB_OUTPUT
  - name: Check result
    if: steps.run-cmd.outputs.exit_code != '0'
    run: echo "Script failed"
```

## Examples

```yaml
# Test failure
# Error: Process completed with exit code 1
# Fix: fix the failing test or add continue-on-error: true

# Missing script
# Error: ./deploy.sh: No such file or directory
# Fix: ensure the script is committed and executable
```

## Related Errors

- [Timeout Error]({{< relref "/tools/github-actions/timeout-error8" >}}) — job exceeded timeout
- [Secret Error]({{< relref "/tools/github-actions/secret-error" >}}) — secret not found
