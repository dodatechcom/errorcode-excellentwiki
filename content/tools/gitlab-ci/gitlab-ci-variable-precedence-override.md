---
title: "[Solution] GitLab CI Variable Precedence Override"
description: "Fix GitLab CI variable precedence override issues when unexpected variable values take priority over intended configurations."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Variable Precedence Override

Variable precedence issues occur when a CI/CD variable from a higher-precedence source silently overrides the intended value, causing unexpected job behavior.

## Common Causes

- Pipeline variable overrides project-level variable
- Group variable overrides project variable unintentionally
- Instance-level variable takes precedence over project settings
- Job-level variable overrides global variable in unintended way

## How to Fix

### Solution 1: Understand variable precedence

Variables follow this precedence (highest first):

1. Trigger variables
2. Pipeline variables
3. Project-level variables
4. Group-level variables
5. Instance-level variables
6. Deployment variables

```yaml
# Job-level variable has highest precedence in .gitlab-ci.yml
build_job:
  variables:
    NODE_ENV: production
  script:
    - echo $NODE_ENV
```

### Solution 2: Use protected and masked flags

```yaml
# In Settings > CI/CD > Variables
# Protect: Only available on protected branches/tags
# Mask: Hidden in job logs
SECRET_KEY:
  value: "secret"
  protected: true
  masked: true
```

### Solution 3: Debug variable values

```yaml
debug_variables:
  stage: .pre
  script:
    - env | sort | grep -E "^(NODE_ENV|API_KEY|DB_HOST)="
```

## Examples

```
Expected NODE_ENV=staging but got NODE_ENV=production
```

## Prevent It

- Document all variable sources and their precedence
- Use protected variables for branch-specific values
- Audit variables regularly in project, group, and instance settings
