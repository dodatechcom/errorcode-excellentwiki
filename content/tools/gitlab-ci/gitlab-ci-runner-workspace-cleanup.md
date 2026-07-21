---
title: "[Solution] GitLab CI Runner Workspace Cleanup"
description: "Fix GitLab CI runner workspace cleanup failures when the runner cannot remove temporary build directories after a job."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Runner Workspace Cleanup

Workspace cleanup failures occur when the runner cannot remove temporary files and directories after a job completes, leading to disk space exhaustion.

## Common Causes

- Job creates files owned by a different user
- Read-only file system or restricted permissions on build directory
- Symlinks pointing outside the workspace root
- Large temporary files exceeding cleanup timeout
- Docker executor volumes not properly unmounted

## How to Fix

### Solution 1: Clean up within the job

Add explicit cleanup in your job script:

```yaml
test_job:
  after_script:
    - rm -rf node_modules/
    - rm -f /tmp/*.log
    - docker system prune -f
```

### Solution 2: Configure runner cleanup settings

Adjust the runner's cleanup behavior in `config.toml`:

```toml
[[runners]]
  [runners.docker]
    disable_cache = false
    volumes = ["/cache", "/tmp/build:/tmp/build"]
```

### Solution 3: Use a dedicated disk partition

Isolate build directories on a separate partition that can be wiped periodically:

```bash
# Mount a dedicated build partition
mount /dev/sdb1 /home/gitlab-runner/builds
```

## Examples

```
WARNING: Failed to clean workspace: permission denied
ERROR: Unable to remove directory /builds/project/-/0
```

## Prevent It

- Use `after_script` for job-specific cleanup
- Monitor disk usage on runner hosts
- Set up cron jobs to clean stale build directories
