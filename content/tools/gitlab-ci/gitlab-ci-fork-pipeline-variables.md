---
title: "[Solution] GitLab CI Fork Pipeline Variables"
description: "Fix GitLab CI fork pipeline variable issues when forked pipelines cannot access protected variables from the parent project."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Fork Pipeline Variables

Fork pipeline variables are restricted by default to prevent secrets from leaking to untrusted code. Forked pipelines only have access to unprotected CI/CD variables.

## Common Causes

- Protected variables are not available in fork pipelines
- Fork source does not have permission to access parent project variables
- CI/CD variables are scoped to protected branches only
- Group variables marked as protected are excluded from forks

## How to Fix

### Solution 1: Set variables as non-protected for forks

In **Settings > CI/CD > Variables**, uncheck "Protect variable" for variables forks need:

```yaml
test_job:
  script:
    - echo $PUBLIC_API_KEY  # Available in fork pipelines
    - echo $SECRET_KEY      # Only in parent pipelines
```

### Solution 2: Use parent project trigger instead of fork

Trigger the parent pipeline with specific variables:

```yaml
trigger_parent:
  trigger:
    project: parent-project/main
    strategy: depend
  variables:
    FORK_COMMIT: $CI_COMMIT_SHA
```

### Solution 3: Use `CI_PIPELINE_SOURCE` to detect forks

```yaml
deploy_job:
  script:
    - ./deploy.sh
  rules:
    - if: $CI_PIPELINE_SOURCE == "push" && $CI_PROJECT_NAMESPACE == $CI_PROJECT_ROOT_NAMESPACE
      when: on_success
    - when: manual
```

## Examples

```
WARNING: Variable SECRET_KEY is not available in fork pipelines
```

## Prevent It

- Document which variables are protected
- Use `CI_PROJECT_NAMESPACE` checks for sensitive operations
- Provide non-secret alternatives for fork workflows
