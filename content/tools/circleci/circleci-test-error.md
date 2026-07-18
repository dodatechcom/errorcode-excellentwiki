---
title: "[Solution] CircleCI Test Error"
description: "Fix CircleCI test errors. Learn why this happens and how to resolve it quickly."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# CircleCI Test Error

CircleCI test errors occur when test results fail to parse, upload, or display correctly.

## Why This Happens

- JUnit XML invalid
- Test results missing
- Flaky tests detected
- Parallel split error

## Common Error Messages

- `test_parse_error`
- `test_results_missing`
- `test_flaky`
- `test_split_error`

## How to Fix It

### Solution 1: Generate JUnit XML

Configure your test framework to output JUnit XML:

```yaml
- store_test_results:
    path: test-results
```

### Solution 2: Split tests across containers

Use circleci tests split:

```yaml
- run:
    command: |
      circleci tests glob "**/*_test.rb" | circleci tests split > tests.txt
      bundle exec rspec $(cat tests.txt)
```

### Solution 3: Handle flaky tests

Retry flaky tests automatically:

```yaml
- run:
    command: bundle exec rspec
    no_output_timeout: 5m
```


## Common Scenarios

- **Test results not showing:** Verify the JUnit XML format is correct.
- **Tests timing out:** Increase no_output_timeout.

## Prevent It

- Use JUnit XML format
- Implement test splitting
- Handle flaky tests
