---
title: "[Solution] CircleCI Environment Variable Masking Error"
description: "Fix CircleCI environment variable masking errors when sensitive values are not properly hidden in job output."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Environment Variable Masking Error

Environment variable masking errors occur when CircleCI fails to mask sensitive variable values in job logs, potentially exposing secrets.

## Common Causes

- Variable value is shorter than the minimum masking length
- Variable value contains only characters that cannot be masked
- Variable was set after the masking filter was applied
- Custom environment variable in a Docker layer exposes the value

## How to Fix

### Solution 1: Ensure sufficient variable length

CircleCI requires variables to be at least 8 characters for masking. Set longer values:

```yaml
# In Project Settings > Environment Variables
# Use values like: sk-proj-abc123def456... (longer strings)
```

### Solution 2: Avoid echoing sensitive variables

```yaml
jobs:
  deploy:
    steps:
      - run:
          name: Login to registry
          command: |
            echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
            # Never echo the password directly
```

### Solution 3: Use context-based variables

```yaml
workflows:
  deploy:
    jobs:
      - deploy:
          context:
            - production-secrets
```

## Examples

```
WARNING: Environment variable AWS_SECRET_KEY may not be masked
```

## Prevent It

- Use values longer than 8 characters for sensitive variables
- Never echo secrets directly in scripts
- Use `--password-stdin` for password inputs
