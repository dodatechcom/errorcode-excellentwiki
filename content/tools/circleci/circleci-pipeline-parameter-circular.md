---
title: "[Solution] CircleCI Pipeline Parameter Circular Dependency"
description: "Fix CircleCI pipeline parameter circular dependency errors when parameter definitions reference each other in a loop."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Pipeline Parameter Circular Dependency

Pipeline parameter circular dependency errors occur when parameter values reference other parameters that eventually reference back to the original parameter.

## Common Causes

- Parameter A default references Parameter B, which references Parameter A
- Dynamic parameter expressions create infinite loops
- Parameter values computed from other parameters without proper ordering
- Orbs define parameters that depend on each other

## How to Fix

### Solution 1: Remove circular references

```yaml
# Wrong - circular dependency
parameters:
  env:
    type: string
    default: << pipeline.parameters.region >>  # References region
  region:
    type: string
    default: << pipeline.parameters.env >>    # References env - CIRCULAR

# Fixed
parameters:
  env:
    type: enum
    enum: [staging, production]
    default: staging
  region:
    type: string
    default: us-east-1  # Independent of env
```

### Solution 2: Use static default values

```yaml
parameters:
  debug:
    type: boolean
    default: false
  log_level:
    type: string
    default: info  # No reference to other parameters
```

### Solution 3: Validate parameter definitions

```bash
circleci config validate .circleci/config.yml
circleci config process .circleci/config.yml
```

## Examples

```
Error: Circular parameter dependency detected
Error: Parameter resolution failed: infinite loop
```

## Prevent It

- Keep parameter defaults independent
- Use `circleci config validate` before pushing
- Test parameterized workflows with explicit values
