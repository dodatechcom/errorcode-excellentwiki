---
title: "[Solution] GitLab CI MR Pipeline Trigger Conflict"
description: "Fix GitLab CI merge request pipeline trigger conflicts when multiple pipelines run simultaneously for the same merge request."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI MR Pipeline Trigger Conflict

Merge request pipeline trigger conflicts occur when multiple pipelines (branch, merge request, and merged result) are triggered for the same merge request, causing resource contention and confusing status checks.

## Common Causes

- Both branch and merge request pipelines are enabled
- Merged result pipeline runs alongside regular MR pipeline
- Push to MR branch triggers both branch and MR pipelines
- `CI_MERGE_REQUEST_ID` variable conflicts between pipelines

## How to Fix

### Solution 1: Use rules to prevent duplicate pipelines

```yaml
# Only run on merge request pipelines
job:
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
```

### Solution 2: Disable branch pipelines for MR branches

Navigate to **Settings > CI/CD** and configure:

```yaml
workflow:
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
```

### Solution 3: Use `CI_OPEN_MERGE_REQUESTS` to detect MR context

```yaml
job:
  rules:
    - if: $CI_OPEN_MERGE_REQUESTS != null  # Running in MR context
      when: never  # Skip branch pipeline if MR pipeline exists
    - when: on_success
```

## Examples

```
WARNING: Duplicate pipeline triggered for merge request #42
Pipeline #1234 and #1235 both running for the same commit
```

## Prevent It

- Use `workflow:rules` to control pipeline creation
- Choose either branch or merge request pipelines, not both
- Document pipeline strategy in project CI configuration
