---
title: "[Solution] CircleCI Environment Variable Expansion Error"
description: "Fix CircleCI environment variable expansion errors when variable references in config.yml are not correctly expanded at runtime."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Environment Variable Expansion Error

Environment variable expansion errors occur when variable references in `config.yml` (e.g., `<< pipeline.parameters.env >>` or `$VAR`) are not correctly expanded, leaving literal strings in the configuration.

## Common Causes

- Variable name does not match any defined variable
- Variable is not available in the current pipeline context
- Incorrect expansion syntax for the variable type
- Pipeline parameters used where job-level variables are expected

## How to Fix

### Solution 1: Use correct expansion syntax

```yaml
# Pipeline parameters
echo << pipeline.parameters.env >>

# Job-level variables
echo $MY_VAR

# Workflow variables
echo << pipeline.parameters.branch >>
```

### Solution 2: Define variables before use

```yaml
jobs:
  build:
    environment:
      MY_VAR: "hello"
    steps:
      - run: echo $MY_VAR
```

### Solution 3: Test variable availability

```yaml
jobs:
  debug:
    steps:
      - run:
          name: Show all variables
          command: env | sort
```

## Examples

```
Error: Undefined variable: $MISSING_VAR
Warning: Variable expansion resulted in empty string
```

## Prevent It

- Define all variables before using them
- Use `env` to debug variable values
- Use pipeline parameters for workflow-level values and environment for job-level
