---
title: "[Solution] CircleCI Resource Class CPU Limit"
description: "Fix CircleCI resource class CPU limit errors when jobs exceed the allocated CPU resources for the chosen resource class."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI resource Class CPU Limit

Resource class CPU limit errors occur when a job consumes more CPU resources than allocated for its configured resource class, leading to throttling or termination.

## Common Causes

- Parallel compilation tasks exceed available CPU cores
- Resource class is too small for the workload
- Docker executor has lower CPU limits than machine executor
- Multiple processes compete for CPU time

## How to Fix

### Solution 1: Upgrade resource class

```yaml
jobs:
  build:
    docker:
      - image: cimg/base:current
    resource_class: large  # 4 vCPUs
    steps:
      - run: make build
```

### Solution 2: Limit parallel jobs

```yaml
jobs:
  test:
    docker:
      - image: cimg/node:18.0
    resource_class: medium
    steps:
      - run:
          name: Run tests sequentially
          command: npm test -- --maxWorkers=2
```

### Solution 3: Use machine executor for heavy workloads

```yaml
jobs:
  build:
    machine:
      image: ubuntu-2204:2023.10.1
    resource_class: xlarge
    steps:
      - checkout
      - run: docker build .
```

## Examples

```
Error: Job exceeded resource class CPU limit
Process killed due to excessive CPU usage
```

## Prevent It

- Match resource class to workload requirements
- Use `--maxWorkers` or similar flags to limit parallelism
- Monitor job performance metrics
