---
title: "[Solution] CircleCI Docker Executor Memory Limit"
description: "Fix CircleCI Docker executor memory limit errors when jobs exceed the allocated memory for the chosen resource class."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Docker Executor Memory Limit

Docker executor memory limit errors occur when a job consumes more memory than the allocated limit for its resource class, causing the process to be killed.

## Common Causes

- Build process creates large in-memory data structures
- Test suite runs all tests in parallel without memory limits
- Java or JVM-based builds with insufficient heap size
- Node.js process leaks memory during long-running tasks

## How to Fix

### Solution 1: Upgrade resource class

```yaml
jobs:
  build:
    docker:
      - image: cimg/node:18.0
    resource_class: large  # 4GB memory
    steps:
      - run: npm run build
```

### Solution 2: Limit process memory usage

```yaml
steps:
  - run:
      name: Run tests with memory limit
      command: NODE_OPTIONS="--max-old-space-size=2048" npm test
```

### Solution 3: Use machine executor for memory-heavy tasks

```yaml
jobs:
  build:
    machine:
      image: ubuntu-2204:2023.10.1
    resource_class: large
    steps:
      - checkout
      - run: ./heavy-build.sh
```

## Examples

```
Killed
ERROR: JavaScript heap out of memory
```

## Prevent It

- Monitor memory usage in CI jobs
- Set appropriate JVM or Node.js heap limits
- Use larger resource classes for memory-intensive workloads
