---
title: "[Solution] CircleCI Test Result Storage Path"
description: "Fix CircleCI test result storage path errors when store_test_results cannot find the specified test output files."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Test Result Storage Path

Test result storage path errors occur when `store_test_results` points to a directory that does not contain valid test result XML files.

## Common Causes

- Test result XML files are in a different directory than specified
- Test framework did not generate XML output
- Path points to a file instead of a directory
- XML files have an unsupported format

## How to Fix

### Solution 1: Configure test framework to output XML

```yaml
jobs:
  test:
    steps:
      - run:
          name: Run tests with JUnit output
          command: |
            mkdir -p test-results
            npx jest --reporters=jest-junit
      - store_test_results:
          path: test-results
```

### Solution 2: Verify output path before storing

```yaml
steps:
  - run:
      name: Run tests
      command: pytest --junitxml=test-results/junit.xml
  - run:
      name: Check test results
      command: ls -la test-results/
  - store_test_results:
      path: test-results
```

### Solution 3: Use store_artifacts as backup

```yaml
steps:
  - store_test_results:
      path: test-results
  - store_artifacts:
      path: test-results
      destination: test-reports
```

## Examples

```
Error: store_test_results: path does not contain test results
WARNING: No JUnit test results were found
```

## Prevent It

- Configure test frameworks to output JUnit XML format
- Verify the output path matches the configured location
- Use `store_artifacts` as a fallback for debugging
