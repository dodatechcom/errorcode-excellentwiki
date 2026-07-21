---
title: "[Solution] GitLab CI Manual Job Timeout"
description: "Fix GitLab CI manual job timeout errors when manual jobs exceed the maximum allowed wait time before execution."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Manual Job Timeout

Manual job timeout errors occur when a job marked as `when: manual` is not triggered within the pipeline's expiration period.

## Common Causes

- Manual job waiting too long before being triggered
- Pipeline expiration is shorter than the approval window
- Group or project-level pipeline timeout overrides job settings
- Scheduled pipeline expiration too short for manual approval workflow

## How to Fix

### Solution 1: Set appropriate pipeline timeout

Increase the pipeline expiration in project settings or `.gitlab-ci.yml`:

```yaml
variables:
  CI_PIPELINE_TIMEOUT: "7d"

deploy_production:
  stage: deploy
  when: manual
  script:
    - ./deploy.sh production
```

### Solution 2: Use pipeline expiration settings

Navigate to **Settings > CI/CD > Continuous Integration and Deployment** and increase the pipeline expiration.

### Solution 3: Trigger manual jobs programmatically

```bash
# Using GitLab API to trigger manual job
curl --request POST \
  --header "PRIVATE-TOKEN: $TOKEN" \
  "$CI_API_V4_URL/projects/$CI_PROJECT_ID/pipelines/$CI_PIPELINE_ID/jobs/$JOB_ID/play"
```

## Examples

```
This job is stuck. You can increase the expiration in the pipeline settings.
Pipeline exceeded timeout and was automatically cancelled
```

## Prevent It

- Set pipeline expiration longer than your approval process
- Document manual approval workflows
- Use `allow_failure: true` to prevent pipeline blocking
