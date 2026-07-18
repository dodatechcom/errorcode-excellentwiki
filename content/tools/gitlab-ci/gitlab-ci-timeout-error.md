---
title: "[Solution] GitLab CI Timeout Error"
description: "Fix GitLab CI timeout errors. Learn why this happens and how to resolve it quickly."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# GitLab CI Timeout Error

Timeout errors occur when jobs exceed configured time limits.

## Why This Happens

- Default 1-hour too short
- Pipeline timeout not set
- Infinite loop
- Runner overloaded

## Common Error Messages

- `job_timeout`
- `pipeline_timeout`
- `execution_timeout`
- `stuck_job`

## How to Fix It

### Solution 1: Increase job timeout

Set timeout keyword in the job:

```yaml
my_job:
  timeout: 2h
  script:
    - long-running-task
```

### Solution 2: Set pipeline timeout

Configure global pipeline timeout in Settings > CI/CD > General pipelines.

### Solution 3: Prevent infinite loops

Add explicit exit conditions and maximum iteration counts to scripts.


## Common Scenarios

- **Job stuck pending:** Check runner availability and job queue.
- **Timeout too short:** Increase timeout based on actual execution time.

## Prevent It

- Set job-specific timeouts
- Use pipeline timeout
- Monitor execution times
