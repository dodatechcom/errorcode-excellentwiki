---
title: "[Solution] GitLab CI Rollback Error"
description: "Fix GitLab CI rollback errors. Learn why this happens and how to resolve it quickly."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# GitLab CI Rollback Error

Rollback errors occur when rollback procedures fail to restore previous application state.

## Why This Happens

- Previous image unavailable
- History not preserved
- Command wrong
- Resource conflicts

## Common Error Messages

- `rollback_failed`
- `rollback_not_available`
- `rollback_state_error`
- `rollback_timeout`

## How to Fix It

### Solution 1: Auto-rollback on failure

Use after_script with CI_JOB_STATUS:

```yaml
deploy:
  after_script:
    - if [ "$CI_JOB_STATUS" == "failed" ]; then kubectl rollout undo deployment/myapp; fi
```

### Solution 2: Manual rollback jobs

Create a manual rollback job:

```yaml
rollback:
  when: manual
  script:
    - kubectl rollout undo deployment/myapp
```

### Solution 3: Preserve deployment history

Ensure Kubernetes maintains revision history:

```yaml
spec:
  revisionHistoryLimit: 10
```


## Common Scenarios

- **Manual rollback:** Create with when: manual.
- **Rollback not available:** Check if previous revision exists with `kubectl rollout history`.

## Prevent It

- Test in staging
- Use --record
- Keep images tagged
