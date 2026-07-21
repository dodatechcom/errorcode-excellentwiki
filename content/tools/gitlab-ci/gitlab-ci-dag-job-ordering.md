---
title: "[Solution] GitLab CI DAG Job Ordering Violation"
description: "Fix GitLab CI DAG job ordering violations when the needs-based dependency graph creates circular or invalid execution order."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI DAG Job Ordering Violation

DAG job ordering violations occur when the `needs` keyword creates a circular dependency or references a job that does not exist in the pipeline.

## Common Causes

- Job A needs Job B while Job B needs Job A
- `needs` references a job from a different stage that does not exist
- A job needs itself
- Group-level DAG includes non-existent inherited jobs

## How to Fix

### Solution 1: Map the dependency graph

Draw out your `needs` relationships to find cycles:

```yaml
# Correct - linear dependency
build:
  stage: build
  script: npm run build

test:
  stage: test
  needs: [build]
  script: npm test

deploy:
  stage: deploy
  needs: [test]
  script: ./deploy.sh
```

### Solution 2: Remove circular dependencies

```yaml
# Wrong - circular dependency
job_a:
  needs: [job_b]

job_b:
  needs: [job_a]

# Fixed
job_a:
  needs: []

job_b:
  needs: [job_a]
```

### Solution 3: Use `needs:optional` for non-critical dependencies

```yaml
lint_job:
  needs:
    - job: build
      optional: true
  script:
    - npm run lint
```

## Examples

```
Circular dependency detected: job_a -> job_b -> job_a
needs reference job 'missing_job' which is not defined
```

## Prevent It

- Visualize your DAG using the pipeline graph view
- Use `needs:optional` for soft dependencies
- Validate with CI Lint before pushing
