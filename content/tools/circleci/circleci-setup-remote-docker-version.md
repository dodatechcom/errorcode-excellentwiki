---
title: "[Solution] CircleCI Setup Remote Docker Version"
description: "Fix CircleCI setup_remote_docker version incompatibility errors when the remote Docker version does not support required features."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Setup Remote Docker Version

Setup remote Docker version errors occur when the `setup_remote_docker` step specifies a Docker version that is not available or incompatible with the executor.

## Common Causes

- Requested Docker version is not supported by CircleCI
- Remote Docker is not available for the chosen executor
- Docker version conflict with build tool requirements
- Remote Docker quota exceeded for the organization

## How to Fix

### Solution 1: Use a supported Docker version

```yaml
jobs:
  build:
    docker:
      - image: cimg/base:current
    steps:
      - setup_remote_docker:
          version: 20.10.24  # Use a supported version
```

### Solution 2: Remove version pinning

Let CircleCI choose the default compatible version:

```yaml
steps:
  - setup_remote_docker
```

### Solution 3: Check available versions

```bash
# Check CircleCI documentation for supported versions
# https://circleci.com/docs/docker-versioning/
```

## Examples

```
Error: Requested Docker version is not available
Remote Docker is not supported for this executor
```

## Prevent It

- Use the default Docker version when possible
- Check CircleCI docs for supported version list
- Test remote Docker setup before relying on it
