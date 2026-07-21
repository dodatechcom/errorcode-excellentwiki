---
title: "[Solution] GitLab CI Child Pipeline Retry Error"
description: "Fix GitLab CI child pipeline retry errors when retried child pipelines fail to re-run correctly."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Child Pipeline Retry Error

Child pipeline retry errors occur when a retried child pipeline does not re-execute properly due to stale state, variable mismatches, or artifact dependency issues.

## Common Causes

- Retried child pipeline uses stale artifacts from the parent
- Variables from the parent pipeline are not re-passed on retry
- Downstream child pipeline has dependency on failed state
- Parent pipeline retry does not re-trigger child pipelines

## How to Fix

### Solution 1: Use `needs:artifact` correctly

Ensure child pipelines re-fetch artifacts on retry:

```yaml
child_job:
  needs:
    - job: parent_build
      artifacts: true
  script:
    - ./run-tests.sh
```

### Solution 2: Pass variables explicitly

Re-pass variables when triggering child pipelines:

```yaml
trigger_child:
  trigger:
    include:
      - local: child-pipeline.yml
    strategy: depend
    forward:
      yaml_variables: true
      pipeline_variables: true
```

### Solution 3: Handle retry in child pipeline

Add retry awareness to child pipeline scripts:

```yaml
child_stage:
  script:
    - echo "Pipeline: $CI_PIPELINE_ID"
    - echo "Retry: $CI_PIPELINE_RETRY_COUNT"
    - ./build.sh --force
```

## Examples

```
Downstream pipeline could not be retried: artifact not found
Child pipeline retry failed: missing required variables
```

## Prevent It

- Use `strategy: depend` for child pipeline retries
- Avoid caching critical state between retries
- Test retry scenarios in development pipelines
