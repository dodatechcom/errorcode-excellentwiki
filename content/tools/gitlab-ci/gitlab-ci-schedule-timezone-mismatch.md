---
title: "[Solution] GitLab CI Schedule Timezone Mismatch"
description: "Fix GitLab CI schedule timezone mismatch errors when scheduled pipelines run at incorrect times due to timezone configuration."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Schedule Timezone Mismatch

Schedule timezone mismatch errors occur when scheduled pipelines run at unexpected times because the cron expression uses a different timezone than intended.

## Common Causes

- Cron expression uses UTC but team expects local time
- GitLab instance timezone differs from user expectations
- DST transitions cause jobs to shift by an hour
- Group schedule inherits instance-level timezone

## How to Fix

### Solution 1: Check the instance timezone

Administrators can verify the timezone in GitLab settings:

```bash
# Check GitLab instance timezone
sudo gitlab-rake gitlab:check
```

### Solution 2: Document UTC in schedule comments

```yaml
# .gitlab-ci.yml
# Scheduled pipeline runs at 02:00 UTC (04:00 CEST)
stages:
  - build
  - test
  - deploy
```

### Solution 3: Adjust cron to account for timezone

```bash
# For UTC instance, convert local time:
# Want 06:00 EST -> 11:00 UTC
# Cron expression: 0 11 * * *

# Set in Build > Pipeline Schedules
# Cron: 0 11 * * *
# Timezone: UTC (GitLab 15.3+ supports timezone selection)
```

## Examples

```
Scheduled pipeline ran at unexpected time
Pipeline schedule #456 triggered at 02:00 UTC instead of 02:00 EST
```

## Prevent It

- Set the timezone explicitly in pipeline schedules (GitLab 15.3+)
- Document the expected timezone for all schedules
- Test schedule timing before relying on it for production workflows
