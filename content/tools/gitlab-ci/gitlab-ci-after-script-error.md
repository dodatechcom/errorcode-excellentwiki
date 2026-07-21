---
title: "[Solution] GitLab CI After Script Failed"
description: "Fix GitLab CI after_script failures when the cleanup or reporting step fails after the main job completes."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI After Script Failed

After script failures occur when the `after_script` block encounters an error. By default, `after_script` failures do not affect the main job status but can cause unexpected behavior.

## Common Causes

- `after_script` references variables not available in the after-script context
- Docker service stopped before after_script runs
- Cleanup commands fail due to permission issues
- Network connectivity lost during after_script execution

## How to Fix

### Solution 1: Use allow_failure for after_script

Prevent after_script errors from affecting job status:

```yaml
test_job:
  script:
    - npm test
  after_script:
    - docker system prune -f || true
  after_script_fail_on_error: false
```

### Solution 2: Add error handling in after_script

```yaml
test_job:
  script:
    - npm test
  after_script:
    - |
      if [ -f /tmp/test-output.log ]; then
        echo "Test output available"
      fi
    - docker stop test-container 2>/dev/null || true
```

### Solution 3: Use separate cleanup jobs

```yaml
cleanup:
  stage: .post
  when: always
  script:
    - docker system prune -f
  allow_failure: true
```

## Examples

```
section_start:after_script:Running after script
ERROR: after_script failed
section_end:after_script
```

## Prevent It

- Wrap after_script commands with `|| true` for non-critical steps
- Use `after_script_fail_on_error: false` in GitLab 15.3+
- Keep after_script simple and idempotent
