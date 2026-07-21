---
title: "[Solution] GitLab CI Deploy Freeze Error"
description: "Fix GitLab CI deploy freeze errors that block deployments during protected deployment freeze windows."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Deploy Freeze Error

Deploy freeze errors occur when a deployment is attempted during an active deployment freeze window defined in the project or group settings.

## Common Causes

- Active deployment freeze window is set for the environment
- Pipeline was scheduled before the freeze and runs during it
- Manual deployment triggered during a freeze period
- Group-level freeze overriding project-level settings

## How to Fix

### Solution 1: Check freeze windows

Navigate to **Deploy > Environments > Edit** and review active freeze windows. Temporarily disable or adjust the schedule if needed.

### Solution 2: Skip jobs during freeze

Configure jobs to skip instead of failing during freeze periods:

```yaml
deploy_production:
  stage: deploy
  environment:
    name: production
  rules:
    - if: $CI_DEPLOY_FREEZE == "true"
      when: never
    - when: on_success
  script:
    - ./deploy.sh production
```

### Solution 3: Handle freeze in scripts

Add a check in your deploy script:

```bash
if [ "$CI_DEPLOY_FREEZE" = "true" ]; then
  echo "Deployment is frozen. Skipping."
  exit 0
fi
./deploy.sh production
```

## Examples

```
Deployment to environment 'production' is blocked: deploy freeze is active
```

## Prevent It

- Review freeze windows before scheduling deployments
- Use `rules:when:never` to gracefully handle freeze periods
- Communicate freeze schedules with your team
