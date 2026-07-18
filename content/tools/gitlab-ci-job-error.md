---
title: "[Solution] GitLab CI Job Error"
description: "Fix GitLab CI job errors. Learn why this happens and how to resolve it quickly."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# GitLab CI Job Error

GitLab CI job errors occur when an individual job in the pipeline fails during execution. Common causes include missing dependencies, script errors, resource limits, or environment misconfiguration. Job errors can cascade through the pipeline if downstream jobs depend on the failed job's artifacts or output.

## Why This Happens

- Script command fails with a non-zero exit code
- Missing dependencies or tools not installed in the Docker image
- Insufficient memory or disk space on the runner
- Job exceeds the default 1-hour timeout
- Environment variables not set or incorrectly configured

## Common Error Messages

- `job_failure: job failed with exit code 1`
- `job_stuck: job is stuck for more than 10 minutes`
- `job_cancelled: job was manually cancelled`
- `job_script_error: script error in step 1`

## How to Fix It

### Solution 1: Check job logs for the root cause

Navigate to **CI/CD > Pipelines > Job** and review the full job log. Look for:

- Non-zero exit codes (e.g., `exit code 1`)
- Error messages from the build tool or test framework
- Stack traces from application crashes
- OOM (Out of Memory) kills

Use `set -x` in your scripts for verbose debugging output that shows each command before execution.

### Solution 2: Add error handling to scripts

Use `set -e` to fail fast on the first error and `set -o pipefail` for pipe errors:

```yaml
build_job:
  script:
    - set -eo pipefail
    - echo "Building application..."
    - make clean
    - make build
    - make test
```

This ensures that if any command fails, the entire script stops immediately rather than continuing with potentially broken state.

### Solution 3: Install missing dependencies with before_script

Use `before_script` to install tools your job needs before the main script runs:

```yaml
test_job:
  image: python:3.11
  before_script:
    - pip install -r requirements.txt
    - pip install pytest-cov
  script:
    - pytest --cov=src tests/
```

The `before_script` runs before the main `script` section and its failures also cause the job to fail.

### Solution 4: Adjust job timeout for long-running tasks

Set appropriate timeouts for jobs that need more than the default 1 hour:

```yaml
long_build:
  timeout: 2h
  script:
    - make build-all
    - make test-all
```

The maximum timeout is 24 hours for specific runners. For shared runners, check the runner configuration.


## Common Scenarios

- **Job fails with 'command not found':** Ensure the Docker image includes the required tool, or install it in `before_script` using the package manager.
- **Job is stuck and never starts executing:** Check runner availability and tags. Ensure at least one runner with matching tags is online and not overloaded.

## Prevent It

- Use `before_script` for environment setup and dependency installation
- Set explicit timeouts for jobs that take longer than the default 1 hour
- Use artifacts and dependencies to pass files between jobs efficiently
