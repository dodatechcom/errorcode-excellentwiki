---
title: "[Solution] CircleCI TEE (Trusted Execution) Error"
description: "Fix CircleCI tee (trusted execution) errors. Learn why this happens and how to resolve it quickly."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# CircleCI TEE (Trusted Execution) Error

CircleCI TEE errors occur when trusted execution environment features fail.

## Why This Happens

- TEE not available
- Configuration invalid
- Execution failed
- Security policy error

## Common Error Messages

- `tee_not_available_error`
- `tee_config_error`
- `tee_execution_error`
- `tee_security_error`

## How to Fix It

### Solution 1: Check TEE availability

Verify TEE is available for your plan.

### Solution 2: Configure TEE

Set up trusted execution:

```yaml
jobs:
  build:
    machine:
      image: ubuntu-2204:2023.10.1
    resource_class: large
```

### Solution 3: Verify configuration

Check TEE configuration.


## Common Scenarios

- **TEE not available:** Check plan availability.
- **Configuration invalid:** Review TEE configuration.

## Prevent It

- Use TEE for security
- Verify configuration
- Monitor execution
