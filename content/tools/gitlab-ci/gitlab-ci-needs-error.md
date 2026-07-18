---
title: "[Solution] GitLab CI Needs Error"
description: "Fix GitLab CI needs errors. Learn why this happens and how to resolve it quickly."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# GitLab CI Needs Error

Needs errors occur when job dependency declarations are invalid or circular.

## Why This Happens

- Referenced job not found
- Circular dependency
- Cross-stage reference invalid
- Artifact not available

## Common Error Messages

- `needs_not_found`
- `needs_circular`
- `needs_cross_stage`
- `needs_artifact_missing`

## How to Fix It

### Solution 1: Verify job names

Names must match exactly, case-sensitive. Check with `gitlab-ci-lint`.

### Solution 2: Fix circular dependencies

Ensure the dependency graph is a DAG (directed acyclic graph).

### Solution 3: Disable artifacts when not needed

Prevent unnecessary artifact passing:

```yaml
my_job:
  needs:
    - job: build
      artifacts: false
```


## Common Scenarios

- **Referenced job not found:** Check spelling and ensure the job exists.
- **Artifact not available:** Verify the dependency job produces the expected artifacts.

## Prevent It

- Use needs for explicit deps
- Set artifacts: false when not needed
- Test DAG visually
