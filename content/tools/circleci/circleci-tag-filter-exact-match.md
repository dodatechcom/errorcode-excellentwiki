---
title: "[Solution] CircleCI Tag Filter Exact Match"
description: "Fix CircleCI tag filter exact match errors when workflows triggered by tags do not match the configured tag patterns."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Tag Filter Exact Match

Tag filter exact match errors occur when workflows with `tags: only` or `tags: ignore` do not correctly match the git tag that triggered the pipeline.

## Common Causes

- Tag name does not match the exact pattern specified
- Regex pattern in tag filter uses incorrect syntax
- Tag was pushed with a different format than expected
- `branches` and `tags` filters conflict

## How to Fix

### Solution 1: Use exact tag matching

```yaml
workflows:
  release:
    jobs:
      - build:
          filters:
            tags:
              only: /^v\d+\.\d+\.\d+$/
            branches:
              ignore: /.*/
```

### Solution 2: Test tag pattern matching

```yaml
workflows:
  release:
    jobs:
      - build:
          filters:
            tags:
              only: /^v\d+\.\d+\.\d+(-\w+)?$/
              ignore:
                - /^v\d+\.\d+\.\d+-rc.*$/
```

### Solution 3: Ensure branches are ignored for tag-only workflows

```yaml
workflows:
  release:
    jobs:
      - deploy:
          filters:
            tags:
              only: /^v\d+\.\d+\.\d+$/
            branches:
              ignore: /.*/  # Required to run only on tags
```

## Examples

```
Warning: Tag 'release-1.0' did not match pattern '/^v\d+/'
Workflow did not trigger for tag push
```

## Prevent It

- Document the expected tag format
- Test tag patterns with `echo "tag" | grep -E 'pattern'`
- Always include `branches: ignore: /.*/` for tag-only workflows
