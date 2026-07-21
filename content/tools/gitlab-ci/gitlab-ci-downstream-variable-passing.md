---
title: "[Solution] GitLab CI Downstream Variable Passing"
description: "Fix GitLab CI downstream variable passing errors when triggered child pipelines do not receive expected variables."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Downstream Variable Passing

Downstream variable passing errors occur when a parent pipeline triggers a child or downstream pipeline but the child does not receive the expected variables.

## Common Causes

- Variables not explicitly passed in the trigger configuration
- Downstream pipeline does not define the variable in `variables:` section
- Protected variables excluded from downstream pipeline context
- Variable name mismatch between parent and child

## How to Fix

### Solution 1: Use `forward` to pass variables automatically

```yaml
trigger_downstream:
  trigger:
    project: group/child-project
    strategy: depend
    forward:
      pipeline_variables: true
      yaml_variables: true
```

### Solution 2: Explicitly pass variables in trigger

```yaml
trigger_downstream:
  trigger:
    project: group/child-project
    branch: main
  variables:
    PARENT_COMMIT: $CI_COMMIT_SHA
    BUILD_ARTIFACT: "true"
```

### Solution 3: Define variables in child pipeline

```yaml
# In child project's .gitlab-ci.yml
variables:
  PARENT_COMMIT: ""
  BUILD_ARTIFACT: "false"

deploy_job:
  script:
    - echo "Building from commit: $PARENT_COMMIT"
```

## Examples

```
WARNING: Variable PARENT_COMMIT is empty in downstream pipeline
ERROR: Downstream job cannot access required variable
```

## Prevent It

- Use `forward.pipeline_variables: true` for automatic passing
- Test variable propagation in development pipelines
- Document expected variables for downstream pipelines
