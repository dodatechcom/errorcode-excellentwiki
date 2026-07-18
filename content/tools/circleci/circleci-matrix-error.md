---
title: "[Solution] CircleCI Matrix Error"
description: "Fix CircleCI matrix errors. Learn why this happens and how to resolve it quickly."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# CircleCI Matrix Error

CircleCI matrix errors occur when matrix configurations fail to generate expected job combinations.

## Why This Happens

- Invalid parameters
- Too many combinations
- Variable not supported
- Matrix syntax error

## Common Error Messages

- `matrix_error`
- `matrix_combination_error`
- `matrix_variable_error`
- `matrix_syntax_error`

## How to Fix It

### Solution 1: Configure matrix correctly

Use matrix with parameters:

```yaml
jobs:
  test:
    parameters:
      node-version:
        type: enum
        enum: ["16", "18", "20"]
    docker:
      - image: cimg/node:<< parameters.node-version >>
```

### Solution 2: Limit combinations

Use exclude to skip specific combinations:

```yaml
matrix:
  exclude:
    - node-version: "16"
```

### Solution 3: Use parameters

Define job parameters for matrix support.


## Common Scenarios

- **Too many jobs:** Reduce matrix dimensions.
- **Parameter not found:** Ensure the parameter is defined in the job.

## Prevent It

- Use parameters for matrix
- Monitor job count
- Exclude invalid combos
