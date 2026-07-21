---
title: "[Solution] CircleCI Test Splitting Timing Data"
description: "Fix CircleCI test splitting timing data errors when timing-based splitting produces unbalanced test distribution across containers."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Test Splitting Timing Data

Test splitting timing data errors occur when the timing data used for `--split-by timings` is stale, incomplete, or inaccurate, leading to unbalanced test distribution.

## Common Causes

- Timing data from a previous run is outdated
- New test files have no timing history
- Test framework does not output timing data
- Timing data file is corrupted or empty

## How to Fix

### Solution 1: Generate fresh timing data

```yaml
jobs:
  test:
    parallelism: 4
    steps:
      - run:
          name: Run tests and generate timing data
          command: |
            circleci tests glob "test/**/*.test.js" | circleci tests split --split-by timings --timings-type name
      - store_test_results:
          path: test-results  # Must contain JUnit XML with timing
```

### Solution 2: Use name-based splitting as fallback

```yaml
steps:
  - run:
      name: Split by file name
      command: |
        circleci tests glob "test/**/*.test.js" | circleci tests split
```

### Solution 3: Update timing data regularly

```yaml
steps:
  - run:
      name: Run all tests for timing
      command: |
        circleci tests glob "test/**/*.test.js" | circleci tests split --split-by timings
      when: always
  - store_test_results:
      path: test-results
```

## Examples

```
WARNING: Timing data not available for some test files
Warning: Uneven test distribution detected
```

## Prevent It

- Always use `store_test_results` to update timing data
- Run full test suite periodically to refresh timings
- Use `--split-by name` as a fallback for new projects
