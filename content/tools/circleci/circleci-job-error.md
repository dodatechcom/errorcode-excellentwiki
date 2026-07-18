---
title: "[Solution] CircleCI Job Error"
description: "Fix CircleCI job errors. Learn why this happens and how to resolve it quickly."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# CircleCI Job Error

CircleCI job errors occur when individual jobs fail due to script errors, resource limits, or environment issues.

## Why This Happens

- Command fails
- Resource class too small
- Docker image unavailable
- Working directory missing

## Common Error Messages

- `job_failed`
- `job_timeout`
- `docker_pull_error`
- `resource_limit`

## How to Fix It

### Solution 1: Increase resource class

Use a larger resource class:

```yaml
jobs:
  build:
    resource_class: large
    docker:
      - image: cimg/node:18.0
```

### Solution 2: Fix Docker image issues

Use official CircleCI images:

```yaml
docker:
  - image: cimg/node:18.0
```

### Solution 3: Set working directory

Define working_directory in the job:

```yaml
jobs:
  build:
    working_directory: ~/project
```


## Common Scenarios

- **Command not found:** Check if the tool is installed in the Docker image.
- **Out of memory:** Increase the resource class.

## Prevent It

- Use cimg/* images
- Set resource classes appropriately
- Cache dependencies
