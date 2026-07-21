---
title: "[Solution] GitLab CI Image Pull Policy Conflict"
description: "Resolve GitLab CI image pull policy conflicts when the Docker image pull policy prevents pulling or using cached images."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Image Pull Policy Conflict

Image pull policy conflicts occur when the configured pull policy prevents the runner from pulling or using a locally cached Docker image for a job.

## Common Causes

- `pull_policy` set to `never` but the image is not cached locally
- `pull_policy` set to `always` but the registry is unreachable
- Private registry requires authentication but no credentials configured
- Image tag `latest` combined with aggressive pull policies

## How to Fix

### Solution 1: Use the default pull policy

Remove explicit pull policy to use the runner default:

```yaml
# Let the runner decide pull policy
variables:
  # Do not set DOCKER_PULL_POLICY
```

### Solution 2: Configure per-image pull policy

Set pull policy in the runner configuration:

```toml
[[runners]]
  [runners.docker]
    pull_policy = ["if-not-present"]
```

### Solution 3: Provide registry credentials

For private images, configure authentication in the runner:

```yaml
image:
  name: registry.example.com/my-image:latest
  entrypoint: [""]
variables:
  DOCKER_AUTH_CONFIG: '{"auths":{"registry.example.com":{"auth":"base64encoded"}}}'
```

## Examples

```
ERROR: image pull failed: pull access denied
ERROR: Cannot pull image: policy is set to never
```

## Prevent It

- Use specific image tags instead of `latest`
- Configure `if-not-present` for local development runners
- Set up credential helpers for private registries
