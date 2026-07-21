---
title: "[Solution] GitLab CI Schedule Missing Project"
description: "Fix GitLab CI scheduled pipelines that fail to trigger when the source or target project is missing or inaccessible."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Schedule Missing Project

Scheduled pipelines fail to start when the associated project, its group, or referenced downstream project is missing, archived, or inaccessible.

## Common Causes

- Scheduled pipeline references a deleted or archived project
- Cross-project trigger token points to a non-existent project
- Group-level schedule targets a renamed group
- Project was transferred to a different namespace

## How to Fix

### Solution 1: Verify project existence

Check that all referenced projects exist and are accessible:

```bash
# Using GitLab API
curl --header "PRIVATE-TOKEN: $TOKEN" \
  "https://gitlab.example.com/api/v4/projects/$PROJECT_ID"
```

### Solution 2: Update schedule configuration

Navigate to **Build > Pipeline schedules** and edit the schedule to reference the correct project path.

### Solution 3: Recreate the schedule

If the schedule references a deleted project, delete and recreate it:

```yaml
# In .gitlab-ci.yml, update trigger references
trigger_deploy:
  trigger:
    project: new-namespace/new-project
    branch: main
```

## Examples

```
Pipeline schedule #123 could not be started: project not found
```

## Prevent It

- Use project IDs instead of paths for cross-project references
- Audit pipeline schedules after project transfers
- Set up alerts for archived or deleted projects
