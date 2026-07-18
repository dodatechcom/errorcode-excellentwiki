---
title: "[Solution] GitLab CI Coverage Error"
description: "Fix GitLab CI coverage errors. Learn why this happens and how to resolve it quickly."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# GitLab CI Coverage Error

Coverage errors occur when test coverage results are not captured or displayed.

## Why This Happens

- Regex does not match
- Report not generated
- Below threshold
- Tool not configured

## Common Error Messages

- `coverage_not_found`
- `coverage_parse_error`
- `coverage_threshold`
- `coverage_report_missing`

## How to Fix It

### Solution 1: Configure regex

Set coverage regex in project settings:

```yaml
test:
  coverage: '/Code coverage: (\\d+\\.\\d*)%/'
```

### Solution 2: Generate Cobertura reports

For MR visualization, output Cobertura format:

```yaml
test:
  coverage: '/Code coverage: (\\d+\\.\\d*)%/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura.xml
```

### Solution 3: Set coverage thresholds

Configure minimum coverage in project settings.


## Common Scenarios

- **Coverage not detected:** Verify the regex matches the actual output.
- **Report not found:** Ensure the test tool generates coverage reports.

## Prevent It

- Use Cobertura format
- Test regex
- Set thresholds
