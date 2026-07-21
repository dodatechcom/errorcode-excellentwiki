---
title: "[Solution] CircleCI Workspace Attach Path Error"
description: "Fix CircleCI workspace attach path errors when attach_workspace cannot find the specified directory or files."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Workspace Attach Path Error

Workspace attach path errors occur when `attach_workspace` cannot find files at the specified `at:` path because the workspace was not persisted correctly.

## Common Causes

- `persist_to_workspace` used a different `root` than `attach_workspace` expects
- Workspace was not persisted before the attach step
- File paths in persist do not match what the job needs
- Workspace is larger than the allowed size limit

## How to Fix

### Solution 1: Match root paths between persist and attach

```yaml
# In the persisting job:
persist_to_workspace:
  root: .
  paths:
    - dist

# In the attaching job:
attach_workspace:
  at: .
```

### Solution 2: Verify workspace contents

```yaml
steps:
  - attach_workspace:
      at: .
  - run:
      name: Verify workspace
      command: ls -la dist/
```

### Solution 3: Use relative paths consistently

```yaml
# Persist from build directory
persist_to_workspace:
  root: build
  paths:
    - output

# Attach to the same relative location
attach_workspace:
  at: build
```

## Examples

```
Error: attach_workspace: directory 'dist' does not exist
Error: workspace path validation failed
```

## Prevent It

- Use the same `root` path for persist and attach
- Verify paths exist before persisting
- Check workspace size does not exceed limits
