---
title: "[Solution] CircleCI Branch Filter Regex Error"
description: "Fix CircleCI branch filter regex errors when workflow branch filters do not match expected branch names."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Branch Filter Regex Error

Branch filter regex errors occur when the `branches` filter in a workflow or job uses a regex pattern that does not correctly match or exclude branch names.

## Common Causes

- Regex uses unsupported syntax for CircleCI filters
- Branch name contains special characters not escaped
- `only` and `ignore` filters conflict
- Regex pattern is too broad or too narrow

## How to Fix

### Solution 1: Use simple string matching

```yaml
workflows:
  build:
    jobs:
      - build:
          filters:
            branches:
              only:
                - main
                - develop
                - /release-.*/
```

### Solution 2: Use regex patterns correctly

```yaml
workflows:
  build:
    jobs:
      - build:
          filters:
            branches:
              only: /^main$|^develop$|^release-.*$/
              ignore:
                - /feature-.*/
```

### Solution 3: Handle special branch names

```yaml
workflows:
  build:
    jobs:
      - deploy:
          filters:
            branches:
              only: /^main$/
```

## Examples

```
Error: Invalid branch filter pattern
Warning: Workflow ran on unexpected branch 'release-1.0-hotfix'
```

## Prevent It

- Test regex patterns with a regex tester
- Use simple string matching when possible
- Validate branch filters with `circleci config process`
