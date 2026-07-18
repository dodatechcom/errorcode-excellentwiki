---
title: "[Solution] Docker Compose Volume Permission Denied Error — How to Fix"
description: "Fix Docker Compose volume permission denied errors. Resolve mount permission issues, UID/GID mismatches, and read-only volume failures."
comments: true
---

## What This Error Means

The `permission denied` error on volume mounts occurs when the container process does not have the correct file system permissions to read from or write to a mounted volume. This is caused by UID/GID mismatches between the host user and the container user.

A typical error:

```
error: open /app/config/settings.yml: permission denied
```

Or:

```
PermissionError: [Errno 13] Permission denied:
'/var/log/app/output.log'
```

Or:

```
ERROR: for web  Cannot start service web:
OCI runtime create failed: unable to start container process:
exec: "nginx": permission denied
```

Or:

```
docker: Error response from daemon: error while creating
mount source path: mkdir /host/path: permission denied
```

## Why It Happens

Permission errors occur when:

- **UID/GID mismatch**: The container runs as a different user ID than the one that owns the mounted files on the host.
- **Rootless Docker limitations**: Rootless Docker runs the daemon as a non-root user, restricting which host paths can be mounted.
- **SELinux or AppArmor blocking access**: Mandatory access control systems deny the container access to host paths.
- **Read-only mount with write attempts**: A volume is mounted as `read_only` but the application tries to write to it.
- **Host directory permissions too restrictive**: The mounted host directory has permissions like `700` that only allow the owner access.
- **Named volume ownership issues**: Docker-managed volumes are created with root ownership by default.

## Common Error Messages

### Application cannot write to mounted directory

```
PermissionError: [Errno 13] Permission denied: '/app/data/output.csv'
```

The application inside the container runs as a non-root user but the mounted directory is owned by root.

### Container fails to start entirely

```
docker: Error response from daemon: error while creating mount
source path: mkdir /host/data: permission denied:
container creation: operation not permitted
```

Docker daemon itself cannot create or access the mount source path due to host permissions.

### Read-only filesystem error

```
Read-only file system: '/var/log/app'
```

The volume is mounted as read-only but the application needs to write logs or temporary files.

### SELinux denial

```
SELinux is denjing access to /host/data for container
```

On RHEL/CentOS/Fedora, SELinux blocks the container from accessing the host volume even though Unix permissions are correct.

## How to Fix It

### Solution 1: Fix host directory permissions

Set correct ownership and permissions on the mounted host directory.

```bash
# Find the UID used inside the container
docker compose exec web id
# Output: uid=1000(app) gid=1000(app)

# Set host directory ownership to match
sudo chown -R 1000:1000 ./data

# Or use more permissive permissions for development
chmod -R 777 ./data
```

In the compose file, use the `user` directive to control the container UID:

```yaml
services:
  web:
    image: myapp:latest
    user: "1000:1000"
    volumes:
      - ./data:/app/data
```

### Solution 2: Create a named volume with correct permissions

Named volumes let Docker manage ownership, which avoids host UID conflicts.

```yaml
services:
  web:
    image: myapp:latest
    volumes:
      - app-data:/app/data

volumes:
  app-data:
    driver: local
```

Initialize volume permissions with an init container:

```yaml
services:
  init:
    image: myapp:latest
    user: root
    command: chown -R 1000:1000 /app/data
    volumes:
      - app-data:/app/data

  web:
    image: myapp:latest
    user: "1000:1000"
    volumes:
      - app-data:/app/data
    depends_on:
      - init

volumes:
  app-data:
```

### Solution 3: Fix SELinux context on RHEL/CentOS/Fedora

Add the `:z` or `:Z` suffix to volume mounts for SELinux compatibility.

```yaml
services:
  web:
    volumes:
      - ./data:/app/data:z        # Shared label (multiple containers)
      - ./config:/app/config:Z    # Private label (single container)
```

The `:z` suffix relabels the host path for shared container access. The `:Z` suffix applies a private label for single-container access.

```bash
# Alternative: disable SELinux for testing (not recommended for production)
sudo setenforce 0
```

### Solution 4: Use an entrypoint script to fix permissions at runtime

Run a privileged init step that adjusts ownership before the main process starts.

```dockerfile
# Dockerfile
FROM node:18-alpine

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["node", "server.js"]
```

```bash
#!/bin/bash
# entrypoint.sh
# Fix volume permissions before starting the app
chown -R node:node /app/data
chmod -R 755 /app/data

exec "$@"
```

Compose file:

```yaml
services:
  web:
    build: .
    volumes:
      - ./data:/app/data
```

### Solution 5: Mount as read-only where possible

Restrict mounts to read-only when the application does not need write access.

```yaml
services:
  web:
    volumes:
      - ./config:/app/config:ro     # Read-only
      - ./data:/app/data            # Read-write
      - ./certs:/etc/ssl/certs:ro   # Read-only
```

## Common Scenarios

### Development container cannot write to project directory

A volume-mounted project directory is owned by your host user (UID 1000) but the container runs as root (UID 0) or a different user.

```yaml
# Container expects user 'node' with UID 1024
# But host directory is owned by UID 1000
services:
  web:
    image: node:18-alpine
    user: "1024:1024"
    volumes:
      - .:/app
```

Fix by matching the container user to the host owner:

```yaml
services:
  web:
    image: node:18-alpine
    user: "${UID:-1000}:${GID:-1000}"
    volumes:
      - .:/app
```

```bash
# Set UID/GID in .env file
echo "UID=$(id -u)" >> .env
echo "GID=$(id -g)" >> .env
```

### Docker Desktop permission prompts

Docker Desktop on macOS prompts for file access permissions. Clicking "Deny" causes permission errors inside containers.

```yaml
services:
  web:
    volumes:
      - /Users/me/project:/app  # macOS permission dialog
```

Fix by adding the path in Docker Desktop settings under Resources > File Sharing, or by using a named volume instead.

### Build stage cannot access mounted secrets

During build, mounted build secrets or SSH keys may have restrictive permissions.

```yaml
services:
  web:
    build:
      context: .
      ssh:
        - default
    volumes:
      - ~/.ssh:/root/.ssh:ro
```

The host SSH directory typically has `700` permissions. The build process may fail to read it.

```bash
# Temporarily loosen SSH directory permissions
chmod 755 ~/.ssh
# Restore after build
chmod 700 ~/.ssh
```

## Prevent It

- **Use the `user` directive with explicit UID/GID**: Always specify the container user in the compose file rather than relying on the Dockerfile default. Match this UID to the host directory owner by using environment variables like `${UID:-1000}`.
- **Prefer named volumes over bind mounts for writable data**: Named volumes let Docker manage ownership and permissions. Reserve bind mounts for read-only configuration files or development scenarios where you need host-container file synchronization.
- **Test volume mounts in CI with a fresh user**: Run your compose stack in CI as a non-root user to catch permission issues before they reach production. Add a step that creates the mount directories with the correct ownership and verifies the container can read and write to them.
