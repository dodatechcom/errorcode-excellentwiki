---
title: "[Solution] GitLab CI Job Error"
description: "Fix GitLab CI job errors. Learn why this happens and how to resolve it quickly."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# GitLab CI Job Error

GitLab CI job errors occur when individual jobs fail during execution due to script errors, missing dependencies, or resource limits.

## Why This Happens

- Script command fails
- Missing dependencies
- Insufficient memory
- Job timeout exceeded

## Common Error Messages

- `job_failure: job failed with exit code 1`
- `job_stuck: job is stuck`
- `job_cancelled: job was cancelled`
- `job_script_error`

## How to Fix It

### Solution 1: Check job logs

Navigate to CI/CD > Pipelines > Job and review the full log for error messages and exit codes. Use the raw log option for complete output.

### Solution 2: Install dependencies in before_script

Add dependency installation to before_script:

```yaml
before_script:
  - apt-get update && apt-get install -y build-essential
  - npm ci
```

### Solution 3: Increase memory limits

Set memory limits in the runner config.toml:

```toml
[[runners]]
  [runners.docker]
    memory = "4g"
```


## Common Scenarios

- **Command not found:** Install the tool in before_script or use a different Docker image.
- **Out of memory:** Increase memory limits in runner configuration.

## Prevent It

- Use before_script for setup
- Set explicit timeouts
- Pass files via artifacts
