---
title: "[Solution] GitLab CI Matrix Parameter Expansion"
description: "Fix GitLab CI matrix parameter expansion errors when parallel:matrix variables fail to expand correctly in jobs."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Matrix Parameter Expansion

Matrix parameter expansion errors occur when variables defined in `parallel:matrix` are not correctly expanded in job scripts or configurations.

## Common Causes

- Variable name contains unsupported characters
- Matrix variable value includes special shell characters
- Variable referenced with incorrect syntax in scripts
- Nested matrix arrays have inconsistent dimensions

## How to Fix

### Solution 1: Use simple variable names

Define matrix variables with alphanumeric names:

```yaml
test_job:
  parallel:
    matrix:
      - NODE_VERSION: [16, 18, 20]
        DB_ENGINE: [postgres, mysql]
  script:
    - nvm use $NODE_VERSION
    - npm test
```

### Solution 2: Quote variable values with special characters

```yaml
parallel:
  matrix:
    - TEST_FILTER: ["--grep 'unit tests'", "--grep 'integration tests'"]
```

### Solution 3: Validate matrix combinations

Check that all arrays in a matrix object have the same length:

```yaml
# Correct - same dimensions
parallel:
  matrix:
    - NODE_VERSION: [16, 18]
      OS: [linux, macos]

# Wrong - mismatched
parallel:
  matrix:
    - NODE_VERSION: [16, 18, 20]
      OS: [linux]  # Only 1 element vs 3
```

## Examples

```
undefined variable: $NODE_VERSION in script
matrix expansion failed: inconsistent array lengths
```

## Prevent It

- Keep matrix variable names simple and consistent
- Test matrix expansion with `echo` commands
- Verify all matrix arrays have equal lengths
