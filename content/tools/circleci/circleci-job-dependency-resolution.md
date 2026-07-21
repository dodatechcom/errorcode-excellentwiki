---
title: "[Solution] CircleCI Job Dependency Resolution"
description: "Fix CircleCI job dependency resolution errors when workflow jobs cannot resolve their required dependencies."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Job Dependency Resolution

Job dependency resolution errors occur when the workflow engine cannot determine the correct execution order for jobs due to circular or missing dependencies.

## Common Causes

- Job `requires` references a non-existent job name
- Circular dependency between two or more jobs
- Job name in `requires` does not match the defined job name
- Inherited job from orb has conflicting dependencies

## How to Fix

### Solution 1: Verify job names match exactly

```yaml
workflows:
  build-test:
    jobs:
      - build
      - test:
          requires:
            - build  # Must match the job name exactly
```

### Solution 2: Break circular dependencies

```yaml
# Wrong - circular
jobs:
  job_a:
    steps:
      - run: echo "a"
  job_b:
    steps:
      - run: echo "b"

workflows:
  main:
    jobs:
      - job_a:
          requires: [job_b]
      - job_b:
          requires: [job_a]

# Fixed - common ancestor
workflows:
  main:
    jobs:
      - prepare
      - job_a:
          requires: [prepare]
      - job_b:
          requires: [prepare]
```

### Solution 3: Use approval for manual triggers

```yaml
workflows:
  deploy:
    jobs:
      - build
      - test:
          requires: [build]
      - deploy:
          type: approval
          requires: [test]
```

## Examples

```
Error: Workflow contains circular dependency
Error: Job 'test' requires unknown job 'build'
```

## Prevent It

- Validate workflow configuration with the CircleCI config validator
- Use exact job names in `requires`
- Test workflows locally with `circleci config process`
