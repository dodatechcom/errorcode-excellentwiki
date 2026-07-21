---
title: "[Solution] CircleCI Scheduled Pipeline Cron Error"
description: "Fix CircleCI scheduled pipeline cron expression errors when scheduled workflows do not trigger at the expected times."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Scheduled Pipeline Cron Error

Scheduled pipeline cron errors occur when the cron expression used for scheduled workflows does not trigger at the expected times or does not trigger at all.

## Common Causes

- Cron expression syntax is invalid
- Cron uses UTC but team expects a different timezone
- Scheduled workflow is disabled or paused
- Cron expression has too many or too few fields

## How to Fix

### Solution 1: Use correct cron syntax

CircleCI uses standard 5-field cron expressions:

```yaml
workflows:
  scheduled-build:
    when:
      cron: "0 2 * * 1-5"  # 02:00 UTC on weekdays
      branches:
        only:
          - main
    jobs:
      - build
```

### Solution 2: Account for UTC timezone

```bash
# CircleCI runs cron in UTC
# For 08:00 EST = 13:00 UTC
cron: "0 13 * * *"
```

### Solution 3: Test the cron expression

```bash
# Validate cron expression
echo "0 2 * * 1-5" | crontab -T - 2>/dev/null || echo "Valid syntax"
```

## Examples

```
Error: Invalid cron expression '0 2 * *'
Scheduled workflow did not trigger at expected time
```

## Prevent It

- Verify cron expressions with a cron calculator
- Document the timezone for all scheduled workflows
- Test scheduled workflows by running them manually first
