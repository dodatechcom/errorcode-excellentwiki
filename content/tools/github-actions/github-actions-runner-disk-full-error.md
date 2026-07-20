---
title: "[Solution] GitHub Actions Runner Disk Full Error"
description: "Fix GitHub Actions runner disk full errors causing workflow failures."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Runner disk full errors occur when the runner machine runs out of disk space:

```
Error: ENOSPC: System limit for number of file descriptors reached
No space left on device
```

## Common Causes

- Docker images and layers consuming disk space.
- Build artifacts accumulating over time.
- Logs and temporary files not being cleaned up.

## How to Fix

**Clean Docker resources:**

```bash
docker system prune -af
docker volume prune -f
```

**Add cleanup step to workflow:**

```yaml
steps:
  - name: Free disk space
    if: always()
    run: |
      rm -rf node_modules .next dist build
      docker system prune -f
```

## Examples

```yaml
# Add free disk space step
steps:
  - name: Free disk space
    uses: jlumbroso/free-disk-space@main
    with:
      docker-images: true
      swap-storage: true
```
