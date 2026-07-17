---
title: "[Solution] Docker Compose Volume Error — Fix Mount Failed"
description: "Fix Docker Compose volume mount failed errors. Resolve permission issues, path errors, and volume driver configuration problems."
---

## What This Error Means

Volume mount errors mean Docker Compose cannot attach a volume to a container. The volume source path does not exist, permissions prevent access, or the volume driver is misconfigured.

A typical error:

```
Error response from daemon: error while creating mount source path:
mkdir /host/path: permission denied
```

Or:

```
Error: Mounts denied: The path /path/to/data is not shared from the host
and is not known to Docker
```

## Why It Happens

Volume mount errors occur when:

- **Source path does not exist**: The host directory specified in the mount is not present.
- **Permission denied**: Docker cannot read or write to the source path.
- **Docker Desktop sharing**: On macOS/Windows, the path is not in Docker Desktop's shared directories.
- **Named volume conflicts**: A named volume already exists with different configuration.
- **SELinux restrictions**: SELinux blocks container access to host paths.
- **Bind mount vs named volume confusion**: Using the wrong syntax for the desired mount type.

## How to Fix It

**Step 1: Create the missing host directory**

```bash
mkdir -p /path/to/data
chmod 755 /path/to/data
```

**Step 2: Fix volume syntax**

```yaml
services:
  db:
    volumes:
      # Bind mount (host path)
      - ./data:/var/lib/postgresql/data

      # Named volume (Docker managed)
      - db-data:/var/lib/postgresql/data

      # Read-only mount
      - ./config:/etc/app/config:ro

volumes:
  db-data:
```

**Step 3: Fix SELinux permissions (Linux)**

```bash
# Add :Z for private mount (single container)
volumes:
  - ./data:/var/lib/postgresql/data:Z

# Add :z for shared mount (multiple containers)
volumes:
  - ./data:/var/lib/postgresql/data:z
```

**Step 4: Fix Docker Desktop shared directories**

On macOS/Windows, add the path to Docker Desktop shared resources in Settings > Resources > File Sharing.

**Step 5: Fix named volume ownership**

```yaml
services:
  app:
    volumes:
      - app-data:/data

volumes:
  app-data:
    driver: local
```

Fix ownership after creation:

```bash
docker compose run --rm app chown -R 1000:1000 /data
```

**Step 6: Verify volume configuration**

```bash
docker compose config
docker volume ls
docker volume inspect <volume_name>
```

## Common Mistakes

- **Using bind mounts with relative paths**: Relative paths are relative to the compose file location. Use absolute paths for clarity.
- **Forgetting to create host directories**: Bind mounts do not auto-create source directories.
- **Not setting correct permissions**: Containers run as specific users; ensure host paths are accessible.
- **Using named volumes for configuration files**: Named volumes are for persistent data. Use bind mounts for config files.

## Related Pages

- [Docker Compose Build Error](/tools/docker-compose/docker-compose-build-error/) — Image build failures
- [Docker Compose Network Error](/tools/docker-compose/docker-compose-network-error/) — Network connectivity issues
- [Kubectl Pod Pending](/tools/kubectl/kubectl-pod-pending/) — Pod scheduling issues
