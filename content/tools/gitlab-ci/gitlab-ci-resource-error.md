---
title: "[Solution] GitLab CI Resource Error"
description: "Fix GitLab CI resource errors. Learn why this happens and how to resolve it quickly."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# GitLab CI Resource Error

Resource errors occur when jobs fail due to insufficient runner resources.

## Why This Happens

- Out of disk space
- OOM error
- CPU contention
- Artifact storage full

## Common Error Messages

- `resource_exhausted`
- `memory_limit`
- `cpu_limit`
- `disk_space`

## How to Fix It

### Solution 1: Configure runner limits

Set resource limits in runner config.toml:

```toml
[[runners]]
  [runners.docker]
    memory = "4g"
    cpus = 2
```

### Solution 2: Use resource groups

Prevent concurrent deployments:

```yaml
deploy:
  resource_group: production
```

### Solution 3: Monitor resource usage

Track runner metrics with Prometheus integration.


## Common Scenarios

- **Use resource groups:** Prevent contention between jobs.
- **OOM killed:** Increase memory limits or optimize job memory usage.

## Prevent It

- Monitor usage
- Use resource groups
- Scale runners
