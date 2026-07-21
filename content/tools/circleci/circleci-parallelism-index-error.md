---
title: "[Solution] CircleCI Parallelism Index Error"
description: "Fix CircleCI parallelism index errors when the CIRCLE_NODE_INDEX variable does not correctly partition work across containers."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI parallelism Index Error

Parallelism index errors occur when `CIRCLE_NODE_INDEX` is used incorrectly to partition work, causing duplicate or missed test execution across parallel containers.

## Common Causes

- Manual partitioning logic uses incorrect modulo arithmetic
- Index does not correspond to actual container number
- Test framework does not support CI parallel indexing
- Glob expansion produces different file lists on different containers

## How to Fix

### Solution 1: Use CircleCI test splitting

```yaml
jobs:
  test:
    docker:
      - image: cimg/node:18.0
    parallelism: 4
    steps:
      - checkout
      - run:
          name: Run split tests
          command: |
            TESTS=$(circleci tests glob "test/**/*.test.js" | circleci tests split)
            npx jest $TESTS
```

### Solution 2: Use CIRCLE_NODE_INDEX manually

```yaml
steps:
  - run:
      name: Run tests for this container
      command: |
        TOTAL=4
        INDEX=$CIRCLE_NODE_INDEX
        TEST_FILE=$(ls test/*.js | sed -n "$((INDEX + 1))p")
        npx jest $TEST_FILE
```

### Solution 3: Use parallelism with matrix

```yaml
jobs:
  test:
    docker:
      - image: cimg/node:18.0
    parallelism: 3
    steps:
      - checkout
      - run:
          name: Test container $CIRCLE_NODE_INDEX of $CIRCLE_TOTAL_PARALLELISM
          command: npm test
```

## Examples

```
Error: CIRCLE_NODE_INDEX not set in parallel job
WARNING: Test container 3 ran 50 tests while container 0 ran 200
```

## Prevent It

- Use `circleci tests split` for automatic partitioning
- Balance test execution across containers
- Verify parallelism configuration matches job setup
