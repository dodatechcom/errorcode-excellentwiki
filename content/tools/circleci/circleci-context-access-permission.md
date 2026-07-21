---
title: "[Solution] CircleCI Context Access Permission"
description: "Fix CircleCI context access permission errors when jobs cannot read environment variables from restricted contexts."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Context Access Permission

Context access permission errors occur when a job attempts to use a context that is restricted by organization-level or context-level restrictions.

## Common Causes

- Context is restricted to specific projects but the current project is not allowed
- Context is associated with a different organization
- Context was deleted or renamed
- Context has environment variable restrictions that exclude the job

## How to Fix

### Solution 1: Update context restrictions

Navigate to **Organization Settings > Contexts** and add the project to the allowed list:

```yaml
workflows:
  deploy:
    jobs:
      - deploy:
          context:
            - production-secrets  # Must be accessible to this project
```

### Solution 2: Use project-level variables instead

```yaml
jobs:
  deploy:
    environment:
      API_KEY: $PROJECT_API_KEY  # Project-level variable
    steps:
      - run: deploy.sh
```

### Solution 3: Verify context exists

```bash
# List contexts via API
curl -H "Circle-Token: $TOKEN" \
  "https://circleci.com/api/v2/context"
```

## Examples

```
Error: Context 'production-secrets' is not available to this project
Error: Unauthorized access to context environment variables
```

## Prevent It

- Document which contexts are available to which projects
- Use project-level variables for project-specific secrets
- Review context restrictions after project transfers
