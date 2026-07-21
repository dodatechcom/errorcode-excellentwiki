---
title: "[Solution] GitLab CI Coverage Report Format Error"
description: "Fix GitLab CI coverage report format errors when the coverage output does not match the expected regex pattern."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Coverage Report Format Error

Coverage report format errors occur when the job output does not match the regex pattern defined in the `coverage` keyword, so GitLab cannot parse the coverage percentage.

## Common Causes

- Coverage regex pattern does not match the actual output format
- Test tool outputs coverage in an unexpected locale or format
- Coverage report is written to a file instead of stdout
- Multiple coverage lines in output confuse the parser

## How to Fix

### Solution 1: Match the regex to actual output

Test your regex against the actual coverage output:

```bash
# Run tests and check output
npm test -- --coverage 2>&1 | grep -oP 'Statements\s*:\s*(\d+\.?\d*)%'
```

### Solution 2: Configure coverage regex in `.gitlab-ci.yml`

```yaml
test_job:
  script:
    - npm test -- --coverage
  coverage: '/Statements\s*:\s*(\d+\.?\d*)%/'
```

### Solution 3: Use coverage reports

Use `artifacts:reports:coverage_report` for Cobertura format:

```yaml
test_job:
  script:
    - npm test -- --coverage
  coverage: '/Lines\s*:\s*(\d+\.?\d*)%/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml
```

## Examples

```
Coverage regex did not match any lines in job output
```

## Prevent It

- Test the regex pattern against actual test output
- Use `grep -P` locally to verify the pattern
- Use structured coverage reports for MR comparisons
