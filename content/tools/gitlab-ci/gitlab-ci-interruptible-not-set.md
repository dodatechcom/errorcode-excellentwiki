---
title: "[Solution] GitLab CI Interruptible Not Set"
description: "Resolve interruptible keyword issues in GitLab CI."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Interruptible Not Set

Resolve interruptible keyword issues in GitLab CI. This error occurs when GitLab CI encounters configuration or execution problems.

## Common Causes

- Incorrect `.gitlab-ci.yml` configuration
- Missing or invalid variables
- Runner not available or offline
- Permission or access issues

## How to Fix

### Solution 1: Validate Configuration

Check your `.gitlab-ci.yml` syntax using the GitLab CI Lint tool:

```yaml
# .gitlab-ci.yml example
stages:
  - build
  - test
  - deploy

build_job:
  stage: build
  script:
    - echo "Building..."
```

### Solution 2: Check Runner Status

```bash
# List registered runners
gitlab-runner list

# Verify runner is online
gitlab-runner verify
```

### Solution 3: Review Pipeline Logs

Navigate to your pipeline in GitLab and review the job logs for specific error messages.

## Example

```yaml
# Correct configuration example
stages:
  - build

build_job:
  stage: build
  image: node:18
  script:
    - npm install
    - npm run build
```

## Related Links

- [GitLab CI Documentation](https://docs.gitlab.com/ee/ci/)
- [GitLab CI Troubleshooting](https://docs.gitlab.com/ee/ci/troubleshooting.html)
