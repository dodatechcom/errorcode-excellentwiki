---
title: "[Solution] CircleCI Machine Executor Boot Timeout"
description: "Fix CircleCI machine executor boot timeout errors when the VM fails to start within the expected time limit."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Machine Executor Boot Timeout

Machine executor boot timeout errors occur when the virtual machine for the `machine` executor does not start within CircleCI's timeout window.

## Common Causes

- High demand on CircleCI's VM fleet causes slow provisioning
- Machine image is too large or not cached
- Organization has too many concurrent machine executor jobs
- Network latency delays VM initialization

## How to Fix

### Solution 1: Use a lighter machine image

```yaml
jobs:
  build:
    machine:
      image: ubuntu-2204:2023.10.1  # Use a recent, cached image
    steps:
      - checkout
      - run: make build
```

### Solution 2: Reduce concurrent machine jobs

```yaml
workflows:
  build:
    jobs:
      - docker-build  # Use docker executor where possible
      - test:
          requires: [docker-build]
```

### Solution 3: Retry with backoff

```yaml
jobs:
  build:
    machine:
      image: ubuntu-2204:2023.10.1
    steps:
      - run:
          name: Build with retry
          command: |
            for i in 1 2 3; do
              make build && break || sleep 10
            done
```

## Examples

```
Error: Machine executor timed out waiting for VM to start
ERROR: Failed to provision machine instance
```

## Prevent It

- Use Docker executor when machine features are not needed
- Avoid peak hours for machine-heavy workflows
- Use resource_class to allocate appropriate VM size
