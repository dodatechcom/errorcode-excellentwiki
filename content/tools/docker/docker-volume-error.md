---
title: "[Solution] Docker Volume Error — Volume not found"
description: "Fix Docker 'Volume not found' error. Create, inspect, and recover missing Docker volumes."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "docker"
tags: ["docker", "containers", "volumes", "storage", "data-persistence"]
severity: "error"
weight: 6
---

# ERROR: Volume not found

## Error Message

```
Error: No such volume: myapp_data

Error response from daemon: get myapp_data: no such volume
```

This error occurs when Docker cannot locate a named volume that a container or Compose file references. The volume may have been deleted, never created, or referenced with a typo.

## Common Causes

- The volume was removed with `docker volume rm` or `docker volume prune`
- The volume name in the Compose file does not match any existing volume
- The container references an anonymous volume from a previous run that was cleaned up
- Running `docker compose down -v` deleted project volumes

## Solutions

### Solution 1: Create the Volume Manually

Create the missing volume with the exact name your container or Compose file expects. Docker will then use it on the next run.

```bash
docker volume create myapp_data
docker compose up -d
```

### Solution 2: Let Docker Create It Automatically

Remove any explicit volume name references from your Compose file and let Docker generate the volume using the project name prefix.

```yaml
services:
  db:
    image: postgres:16
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:
```

```bash
docker compose up -d
```

### Solution 3: Recover Data from a Backup

If the volume contained important data and was accidentally deleted, you can restore from a backup tarball into a new volume.

```bash
docker volume create myapp_data_restored
docker run --rm -v myapp_data_restored:/data -v $(pwd):/backup alpine   tar xzf /backup/myapp_data_backup.tar.gz -C /data
docker compose up -d
```

### Solution 4: Inspect All Existing Volumes

List all volumes to verify what actually exists and identify naming mismatches.

```bash
docker volume ls
docker volume inspect myapp_data
```

## Prevention Tips

- Never run `docker compose down -v` in production without checking what volumes are removed
- Back up important volumes regularly using `docker run` with a tarball approach
- Document volume names and their purposes in your project README
- Use explicit volume definitions in `docker-compose.yml` to avoid orphaned anonymous volumes

## Related Errors

- [Docker Mount Failed]({{< relref "/tools/docker/mount-failed" >}}) — bind mount failures
- [Docker Permission Denied]({{< relref "/tools/docker/permission-denied-overlay" >}}) — permission issues with volumes
