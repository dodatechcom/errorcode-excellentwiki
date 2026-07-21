---
title: "[Solution] GitLab CI Runner Registration Revoked"
description: "Fix GitLab CI runner registration revoked errors when a runner's authentication token has been invalidated."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Runner Registration Revoked

Runner registration revoked errors occur when a runner's registration token has been removed from the GitLab instance, preventing the runner from picking up jobs.

## Common Causes

- Admin revoked the runner registration token
- Runner was removed from the project or group settings
- Registration token expired after the grace period
- Runner configuration references a deleted project

## How to Fix

### Solution 1: Re-register the runner

Obtain a new registration token and re-register:

```bash
gitlab-runner register \
  --url https://gitlab.example.com \
  --token NEW_RUNNER_TOKEN \
  --executor docker \
  --docker-image alpine:latest
```

### Solution 2: Use the new runner creation workflow

GitLab recommends using runner authentication tokens instead:

```bash
# Create runner in UI, get auth token
gitlab-runner register \
  --url https://gitlab.example.com \
  --token glrt-YOUR_AUTH_TOKEN \
  --executor shell
```

### Solution 3: Check runner status

```bash
gitlab-runner list
gitlab-runner verify
```

## Examples

```
ERROR: Registering runner... failed   runner=xxxxx
Runner configuration error: token is not valid
```

## Prevent It

- Use authentication tokens instead of registration tokens
- Document runner tokens securely
- Monitor runner status in the GitLab UI regularly
