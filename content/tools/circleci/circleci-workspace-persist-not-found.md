---
title: "[Solution] CircleCI Workspace Persist Not Found"
description: "Fix CircleCI workspace persist not found errors when persist_to_workspace fails to save the correct file paths."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Workspace Persist Not Found

Workspace persist errors occur when `persist_to_workspace` cannot find the specified paths to save to the shared workspace.

## Common Causes

- Path specified does not exist at the time of the persist step
- Working directory is different from the expected path
- File was created in a different job without the persist step
- Glob pattern does not match any files

## How to Fix

### Solution 1: Verify paths exist before persisting

```yaml
jobs:
  build:
    steps:
      - checkout
      - run: npm run build
      - run:
          name: Verify build output
          command: ls -la dist/
      - persist_to_workspace:
          root: .
          paths:
            - dist
```

### Solution 2: Use absolute paths

```yaml
persist_to_workspace:
  root: /home/circleci/project
  paths:
    - dist
    - build/output
```

### Solution 3: Check workspace attachment

```yaml
jobs:
  deploy:
    steps:
      - attach_workspace:
          at: .
      - run: ls -la dist/
```

## Examples

```
Error: persist_to_workspace: path 'dist' does not exist
```

## Prevent It

- Always verify paths exist with `ls` before persisting
- Use relative paths from the working directory
- Ensure the persist step runs after the build step
