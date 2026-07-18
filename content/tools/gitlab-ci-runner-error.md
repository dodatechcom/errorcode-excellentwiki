---
title: "[Solution] GitLab CI Runner Error"
description: "Fix GitLab CI runner errors. Learn why this happens and how to resolve it quickly."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# GitLab CI Runner Error

Runner errors occur when GitLab CI runners cannot register, connect, or execute jobs. This blocks all pipeline execution on affected runners and prevents any CI/CD workflows from completing. Runner issues are often the root cause when all jobs in a pipeline remain in pending state.

## Why This Happens

- Runner registration token is invalid or expired
- Runner is offline or cannot reach the GitLab instance
- Runner executor (Docker, Shell, etc.) is misconfigured
- Runner configuration file has syntax errors
- SSL/TLS certificates are not trusted

## Common Error Messages

- `runner_registration_failed: registration token is invalid`
- `runner_offline: runner is not connected to GitLab`
- `runner_job_failure: job failed during execution`
- `runner_auth_error: authentication failed`

## How to Fix It

### Solution 1: Check runner registration status and connectivity

Verify the runner is registered and online:

```bash
gitlab-runner list
gitlab-runner verify
```

The `verify` command checks that each registered runner can communicate with the GitLab instance. If a runner shows as unreachable, check network connectivity and firewall rules.

### Solution 2: Re-register the runner with a fresh token

Obtain a new registration token from **Settings > CI/CD > Runners** and re-register:

```bash
# Unregister old runner
gitlab-runner unregister --url https://gitlab.example.com --token OLD_TOKEN

# Register with new token
gitlab-runner register \
  --url https://gitlab.example.com \
  --token NEW_TOKEN \
  --name my-runner \
  --executor docker \
  --docker-image alpine:latest
```

Registration tokens are project or group-scoped and can be rotated for security.

### Solution 3: Review and fix the runner configuration file

Edit `/etc/gitlab-runner/config.toml` to fix misconfigurations:

```toml
[[runners]]
  name = "my-runner"
  url = "https://gitlab.example.com"
  token = "TOKEN"
  executor = "docker"
  [runners.docker]
    image = "alpine:latest"
    privileged = false
    volumes = ["/cache"]
    shm_size = 0
```

Verify the executor type, image, and volumes are correct for your use case.

### Solution 4: Restart the runner service and check logs

Restart the GitLab Runner service to resolve transient issues:

```bash
sudo gitlab-runner restart
sudo gitlab-runner status
sudo journalctl -u gitlab-runner -f
```

The `-f` flag follows the log output in real-time, which is helpful for debugging startup issues.


## Common Scenarios

- **Runner shows 'cannot verify SSL certificate':** Install the GitLab server's CA certificate on the runner host, or use `--tls-skip-verify` for testing environments only.
- **Runner picks up jobs but immediately fails:** Check Docker daemon status if using the Docker executor. Ensure the required image can be pulled from the registry.

## Prevent It

- Use runner tags to control which jobs run on which runners
- Keep runner registration tokens secure and rotate them periodically
- Monitor runner health with the GitLab Runner Prometheus metrics endpoint
