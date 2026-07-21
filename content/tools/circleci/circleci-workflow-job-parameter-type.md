---
title: "[Solution] CircleCI Workflow Job Parameter Type"
description: "Fix CircleCI workflow job parameter type mismatch errors when parameter values do not match their declared types."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Workflow Job Parameter Type

Workflow job parameter type mismatch errors occur when a value passed to a parameterized job does not match the declared parameter type.

## Common Causes

- String value passed to a boolean parameter
- Number passed to a string parameter without conversion
- Enum parameter receives a value not in the allowed list
- Parameter default value does not match the declared type

## How to Fix

### Solution 1: Match parameter types

```yaml
parameters:
  deploy_env:
    type: enum
    enum: [staging, production]
    default: staging

jobs:
  deploy:
    parameters:
      env:
        type: enum
        enum: [staging, production]
    steps:
      - run: deploy.sh << parameters.env >>

workflows:
  deploy:
    jobs:
      - deploy:
          env: staging  # Must be one of the enum values
```

### Solution 2: Convert types explicitly

```yaml
parameters:
  build_num:
    type: integer
    default: 1

jobs:
  build:
    parameters:
      num:
        type: integer
    steps:
      - run: echo "Build number: << parameters.num >>"
```

### Solution 3: Use correct parameter syntax

```yaml
# String parameter
parameters:
  branch:
    type: string
    default: "main"

# Boolean parameter
parameters:
  debug:
    type: boolean
    default: false
```

## Examples

```
Error: Parameter 'env' expected type 'enum' but received 'string'
Error: Invalid value for parameter 'debug': expected boolean
```

## Prevent It

- Declare parameter types accurately
- Test parameterized workflows locally
- Use `circleci config process` to validate parameter expansion
