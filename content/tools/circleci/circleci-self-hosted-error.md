---
title: "[Solution] CircleCI Self-Hosted Runner Error"
description: "Fix CircleCI self-hosted runner errors. Learn why this happens and how to resolve it quickly."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# CircleCI Self-Hosted Runner Error

CircleCI self-hosted runner errors occur when self-hosted runners fail to register or execute jobs.

## Why This Happens

- Runner not registered
- Resource class not configured
- Executor not available
- Network unreachable

## Common Error Messages

- `self_hosted_error`
- `runner_registration_error`
- `resource_class_error`
- `executor_error`

## How to Fix It

### Solution 1: Register runner

Register the runner with CircleCI:

```bash
circleci runner resource-class create my-resource-class "Description"
circleci runner token create my-token
```

### Solution 2: Configure executor

Set up the executor in config.toml:

```toml
[agent]
  name = "my-runner"
  resource-class = "my-resource-class"
```

### Solution 3: Check runner status

Monitor runner health:

```bash
circleci runner status
```


## Common Scenarios

- **Runner not connecting:** Check network and firewall settings.
- **Job stuck:** Verify the runner is online and has capacity.

## Prevent It

- Monitor runner health
- Set up alerts
- Document runner setup
