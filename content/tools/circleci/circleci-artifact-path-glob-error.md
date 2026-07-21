---
title: "[Solution] CircleCI Artifact Path Glob Error"
description: "Fix CircleCI artifact path glob errors when store_artifacts paths do not match any files produced by the job."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Artifact Path Glob Error

Artifact path glob errors occur when `store_artifacts` references paths that do not exist or glob patterns that do not match any files.

## Common Causes

- Build step did not produce files at the expected location
- Glob pattern syntax is incorrect
- Working directory is different from expected
- File names are case-sensitive and do not match the pattern

## How to Fix

### Solution 1: Verify paths before storing

```yaml
steps:
  - run:
      name: Build
      command: npm run build
  - run:
      name: Check output
      command: ls -la dist/
  - store_artifacts:
      path: dist
      destination: build-output
```

### Solution 2: Use correct glob syntax

```yaml
steps:
  - store_artifacts:
      path: test-results
      destination: test-reports
  - store_artifacts:
      path: coverage/
      destination: coverage-report
```

### Solution 3: Use absolute paths

```yaml
steps:
  - store_artifacts:
      path: /home/circleci/project/dist
      destination: dist
```

## Examples

```
Error: store_artifacts: path 'dist' does not exist
WARNING: No files found matching path pattern
```

## Prevent It

- Verify file paths with `ls` before storing artifacts
- Use `destination` to organize artifacts in the UI
- Use relative paths from the working directory
