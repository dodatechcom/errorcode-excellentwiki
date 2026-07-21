---
title: "[Solution] CircleCI Job Cancellation Race Condition"
description: "Fix CircleCI job cancellation race conditions when parallel jobs are cancelled simultaneously and leave resources in an inconsistent state."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Job Cancellation Race Condition

Job cancellation race conditions occur when multiple parallel jobs are cancelled at the same time, leaving shared resources (caches, workspaces, deployments) in inconsistent states.

## Common Causes

- Workflow cancellation stops all jobs simultaneously
- Jobs share a context and write conflicting state
- Cache saved by a cancelled job may be incomplete
- Deployment partially completes before cancellation

## How to Fix

### Solution 1: Use idempotent operations

Ensure jobs can be safely retried or cancelled:

```yaml
jobs:
  deploy:
    steps:
      - run:
          name: Deploy with rollback
          command: |
            ./deploy.sh || ./rollback.sh
```

### Solution 2: Add cleanup on cancellation

```yaml
jobs:
  deploy:
    steps:
      - run:
          name: Deploy
          command: ./deploy.sh
      - run:
          name: Cleanup on failure
          when: on_fail
          command: ./cleanup.sh
```

### Solution 3: Use resource groups for serial execution

```yaml
workflows:
  deploy:
    jobs:
      - deploy:
          context:
            - production
```

## Examples

```
Error: Workflow was cancelled while jobs were running
WARNING: Cache may be incomplete due to job cancellation
```

## Prevent It

- Design jobs to be idempotent and resumable
- Use `when: on_fail` steps for cleanup
- Avoid shared mutable state between parallel jobs
