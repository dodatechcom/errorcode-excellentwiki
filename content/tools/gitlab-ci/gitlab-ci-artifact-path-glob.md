---
title: "[Solution] GitLab CI Artifact Path Glob"
description: "Fix GitLab CI artifact path glob errors when glob patterns do not match any files in the workspace."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Artifact Path Glob

Artifact path glob errors occur when the specified glob patterns in the `artifacts.paths` configuration do not match any actual files produced by the job.

## Common Causes

- Typo in the artifact path pattern
- Working directory differs from expected output location
- Build step has not produced files yet at the artifact stage
- Case sensitivity mismatch between pattern and file names
- Glob pattern syntax incompatible with GitLab's implementation

## How to Fix

### Solution 1: Verify file paths with a debug step

Add a step to list files before the job ends:

```yaml
build_job:
  script:
    - npm run build
    - find dist/ -type f | head -20
  artifacts:
    paths:
      - dist/
```

### Solution 2: Use correct glob syntax

GitLab supports standard glob patterns:

```yaml
artifacts:
  paths:
    - "dist/**/*.js"
    - "build/coverage/*.html"
    - "test-results/**/report.xml"
```

### Solution 3: Set the correct working directory

Ensure the build produces files in the expected location:

```yaml
build_job:
  before_script:
    - pwd
    - ls -la
  script:
    - cd /tmp/build && npm run build
  artifacts:
    paths:
      - /tmp/build/dist/
```

## Examples

```
WARNING: No files were found for path dist/
```

## Prevent It

- Test glob patterns with `ls` or `find` in a script step
- Use `artifacts:reports` for structured data like test results
- Keep artifact paths relative to the project root
