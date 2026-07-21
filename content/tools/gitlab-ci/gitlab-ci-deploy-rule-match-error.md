---
title: "[Solution] GitLab CI Deploy Rule Match Error"
description: "Fix GitLab CI deploy rule match errors when deployment rules fail to match any condition in the pipeline."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Deploy Rule Match Error

Rule match errors occur when a deploy job has `rules` configured but none of the conditions match the current pipeline context, causing the job to be skipped unexpectedly.

## Common Causes

- `rules:if` variable does not match current pipeline variables
- Missing `when: on_success` or `when: manual` fallback rule
- Branch name does not match any rule condition
- `changes` rule references files not modified in the MR

## How to Fix

### Solution 1: Add a default rule

Include a fallback rule to handle unmatched conditions:

```yaml
deploy_production:
  stage: deploy
  script:
    - ./deploy.sh
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
      when: on_success
    - when: manual
      allow_failure: true
```

### Solution 2: Debug rule matching

Add a debug job to inspect variables:

```yaml
debug_rules:
  stage: .pre
  script:
    - echo "Branch: $CI_COMMIT_BRANCH"
    - echo "Tag: $CI_COMMIT_TAG"
    - echo "Pipeline source: $CI_PIPELINE_SOURCE"
  rules:
    - when: always
```

### Solution 3: Check variable conditions

```yaml
deploy:
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
    - if: $CI_COMMIT_TAG =~ /^v\d+\.\d+\.\d+$/
```

## Examples

```
This job is excluded by the rules configuration
Job is skipped: no rules matched
```

## Prevent It

- Always include a fallback rule or `when: manual`
- Test rules with `CI_PIPELINE_SOURCE` and branch variables
- Use the CI Lint tool to validate rule syntax
