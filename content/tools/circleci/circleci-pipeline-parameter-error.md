---
title: "[Solution] CircleCI Pipeline Parameter Error"
description: "Fix CircleCI pipeline parameter errors. Learn why this happens and how to resolve it quickly."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# CircleCI Pipeline Parameter Error

CircleCI pipeline parameter errors occur when parameters are missing, invalid, or incorrectly used.

## Why This Happens

- Parameter not defined
- Type mismatch
- Default value missing
- Parameter not accessible

## Common Error Messages

- `parameter_not_found`
- `parameter_type_error`
- `parameter_default_error`
- `parameter_scope_error`

## How to Fix It

### Solution 1: Define parameters

Declare parameters in your config:

```yaml
parameters:
  branch:
    type: string
    default: main
```

### Solution 2: Use parameters in jobs

Reference parameters:

```yaml
jobs:
  build:
    steps:
      - run: echo << pipeline.parameters.branch >>
```

### Solution 3: Trigger with parameters

Use API to trigger with parameters:

```bash
curl -X POST https://circleci.com/api/v2/project/gh/org/repo/pipeline \
  -H "Content-Type: application/json" \
  -d '{"branch": "main"}'
```


## Common Scenarios

- **Parameter not found:** Ensure the parameter is declared in the config.
- **Type mismatch:** Check the parameter type matches the value.

## Prevent It

- Declare parameters
- Validate parameter types
- Document usage
