---
title: "[Solution] CircleCI Branch Error"
description: "Fix CircleCI branch errors. Learn why this happens and how to resolve it quickly."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# CircleCI Branch Error

CircleCI branch errors occur when branch filters prevent jobs from running or run on wrong branches.

## Why This Happens

- Filter syntax wrong
- Branch not matched
- Tag filter missing
- Default branch wrong

## Common Error Messages

- `branch_not_found`
- `filter_syntax_error`
- `tag_filter_error`
- `default_branch_error`

## How to Fix It

### Solution 1: Fix branch filters

Use proper syntax:

```yaml
jobs:
  - deploy:
      filters:
        branches:
          only: main
        tags:
          only: /^v.*/
```

### Solution 2: Handle tags properly

Tags don't run workflows by default. Add tag filters:

```yaml
workflows:
  build-deploy:
    jobs:
      - build:
          filters:
            tags:
              only: /.*/
```

### Solution 3: Check default branch

Verify the default branch name in project settings.


## Common Scenarios

- **Job not running on branch:** Check the branch filter syntax.
- **Tag build not triggering:** Add tag filters to the workflow.

## Prevent It

- Test filters locally
- Document branch strategy
- Handle tags explicitly
