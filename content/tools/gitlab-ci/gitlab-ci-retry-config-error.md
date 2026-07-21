---
title: "[Solution] GitLab CI Retry Config Error"
description: "Fix GitLab CI retry configuration errors when job retry settings cause unexpected re-runs or failures."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Retry Config Error

Retry configuration errors occur when the `retry` keyword is misconfigured, causing jobs to retry on conditions that do not fix the underlying problem.

## Common Causes

- `retry:when` specifies conditions that do not match the failure type
- `retry:max` set too high, causing excessive re-runs
- Retry on `script_failure` retries all script errors including bugs
- Retry conflicts with `allow_failure` or `when: manual`

## How to Fix

### Solution 1: Retry only on transient failures

```yaml
test_job:
  retry:
    max: 2
    when:
      - runner_system_failure
      - stuck_or_timeout_failure
      - api_failure
  script:
    - npm test
```

### Solution 2: Exclude script failures from retry

```yaml
deploy_job:
  retry:
    max: 1
    when:
      - runner_system_failure
  script:
    - ./deploy.sh
```

### Solution 3: Add delay between retries

```yaml
flaky_test:
  retry:
    max: 3
    when:
      - script_failure
  script:
    - ./run-flaky-tests.sh --retry-delay=30
```

## Examples

```
Job retry configuration error: invalid 'when' value
Job retried 5 times but still failing
```

## Prevent It

- Retry only on infrastructure failures, not script errors
- Limit retries to 2-3 for most scenarios
- Test retry behavior in a development pipeline
