---
title: "[Solution] GitLab CI Needs Keyword Dependency"
description: "Fix GitLab CI needs keyword dependency errors when jobs specified in needs do not exist or produce no artifacts."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Needs Keyword Dependency

Needs keyword dependency errors occur when a job references a non-existent job in its `needs` list or when the referenced job produces no artifacts.

## Common Causes

- Job name in `needs` does not match any defined job
- Referenced job was skipped due to `rules` configuration
- Referenced job name changed after the needs was defined
- Inherited job names from includes do not match

## How to Fix

### Solution 1: Verify job names match exactly

```yaml
build:
  stage: build
  script: npm run build

test:
  stage: test
  needs:
    - build  # Must exactly match the job name
  script: npm test
```

### Solution 2: Use optional needs for non-critical dependencies

```yaml
lint:
  stage: test
  needs:
    - job: build
      optional: true
  script: npm run lint
```

### Solution 3: Check if referenced job is skipped

```yaml
# If this job is skipped, downstream jobs with needs will also be skipped
build:
  stage: build
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
  script: npm run build

# Use optional: true to prevent this job from being skipped
test:
  stage: test
  needs:
    - job: build
      optional: true
  script: npm test
```

## Examples

```
Needs reference job 'build' which is not defined in pipeline
Job is skipped: dependency 'build' was skipped
```

## Prevent It

- Use exact job names in `needs`
- Use `optional: true` for non-critical dependencies
- Validate with CI Lint before pushing
