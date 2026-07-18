---
title: "[Solution] CircleCI Executor Error"
description: "Fix CircleCI executor errors. Learn why this happens and how to resolve it quickly."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# CircleCI Executor Error

CircleCI executor errors occur when the specified Docker machine or VM executor cannot be provisioned.

## Why This Happens

- Docker image not found
- Machine image unavailable
- Executor resource invalid
- Network timeout

## Common Error Messages

- `executor_error`
- `docker_not_found`
- `machine_not_available`
- `resource_invalid`

## How to Fix It

### Solution 1: Use official images

Specify valid CircleCI Docker images:

```yaml
executor:
  docker:
    - image: cimg/node:18.0
```

### Solution 2: Check machine images

Use supported machine images:

```yaml
machine:
  image: ubuntu-2204:2023.10.1
```

### Solution 3: Verify resource availability

Check CircleCI status page for outages.


## Common Scenarios

- **Image not found:** Verify the image name and tag exist.
- **Machine unavailable:** Try a different machine image version.

## Prevent It

- Use official CircleCI images
- Check resource availability
- Monitor status page
