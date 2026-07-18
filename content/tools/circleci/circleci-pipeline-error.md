---
title: "[Solution] CircleCI Pipeline Error"
description: "Fix CircleCI pipeline errors. Learn why this happens and how to resolve it quickly."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# CircleCI Pipeline Error

CircleCI pipeline errors occur when pipelines fail to trigger or execute due to configuration issues or platform problems.

## Why This Happens

- Config YAML invalid
- Orb version conflict
- Workflow misconfigured
- Branch filter incorrect

## Common Error Messages

- `pipeline_failed`
- `config_error`
- `workflow_not_running`
- `orb_not_found`

## How to Fix It

### Solution 1: Validate config

Use the CircleCI CLI to validate your config:

```bash
circleci config validate .circleci/config.yml
```

### Solution 2: Check orb versions

Ensure orbs are using compatible versions:

```yaml
orbs:
  node: circleci/node@5.1.0
```

### Solution 3: Review pipeline in UI

Check the CircleCI dashboard for detailed error messages and logs.


## Common Scenarios

- **Pipeline not triggered:** Verify the config YAML is valid and the branch matches filters.
- **Config validation passes but pipeline fails:** Check for runtime errors in job logs.

## Prevent It

- Always validate config before pushing
- Use orb version pinning
- Test with CircleCI local CLI
