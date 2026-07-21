---
title: "[Solution] GitLab CI Secret Variable Scope"
description: "Fix GitLab CI secret variable scope errors when masked or protected variables are not available in pipeline jobs."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Secret Variable Scope

Secret variable scope errors occur when masked or protected CI/CD variables are not accessible in a pipeline job due to scope restrictions.

## Common Causes

- Variable is protected but pipeline runs on an unprotected branch
- Variable is scoped to a specific environment but job lacks environment
- Variable value contains characters that cannot be masked
- Variable is scoped to a protected tag but pipeline is branch-based

## How to Fix

### Solution 1: Check variable protection settings

Navigate to **Settings > CI/CD > Variables** and verify:

- Protected flag matches the branch type
- Environment scope matches the job's environment

```yaml
deploy_production:
  environment:
    name: production
  script:
    - echo $PRODUCTION_SECRET_KEY  # Only available for protected branch + production environment
```

### Solution 2: Create separate variables for different scopes

```yaml
# Project variables:
# SECRET_KEY (protected, env: production) -> value: prod-secret
# SECRET_KEY (protected, env: staging) -> value: staging-secret
# SECRET_KEY (unprotected) -> value: dev-secret
```

### Solution 3: Use environment-specific variables

```yaml
test_job:
  environment:
    name: testing
  script:
    - echo $TEST_API_KEY  # Scoped to testing environment
```

## Examples

```
WARNING: SECRET_KEY is masked but the value cannot be masked
WARNING: variable not available: protected variable on unprotected branch
```

## Prevent It

- Test variable availability with `echo $VAR` in a debug job
- Use `CI_DEBUG_TRACE: "true"` to inspect variable values (carefully)
- Document variable scopes in project README
