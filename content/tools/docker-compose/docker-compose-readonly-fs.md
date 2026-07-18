---
title: "[Solution] Docker Compose Readonly FS Error — Fix Read-Only File System"
description: "Fix Docker Compose read-only filesystem errors when containers cannot write to required paths. Configure writable directories and read-only root filesystems correctly."
---

## What This Error Means

Docker Compose read-only filesystem errors occur when a container is started with `read_only: true` but tries to write to a path not mounted as writable. The filesystem root is read-only and write operations fail.

A typical error:

```
Error: failed to create directory /var/lib/app: read-only file system
```

Or:

```
touch: cannot touch '/tmp/test.txt': Read-only file system
```

## Why It Happens

Read-only FS errors happen when:

- **read_only: true is set**: The container root filesystem is mounted read-only for security.
- **No writable tmpfs or volume for required paths**: The application needs to write to /tmp, /var/run, or /var/log.
- **Application writes to unexpected paths**: The software writes to paths not designated as writable.
- **PID file creation fails**: Services try to create PID files in /var/run without a writable mount.
- **Socket file creation fails**: Unix sockets cannot be created on a read-only filesystem.

## How to Fix It

**Step 1: Identify writable paths needed**

```bash
# From the Dockerfile or error logs, find the paths the app writes to
# Common paths: /tmp, /var/run, /var/log, /var/lib, /run
```

**Step 2: Mount writable tmpfs for temporary paths**

```yaml
services:
  app:
    image: my-app
    read_only: true
    tmpfs:
      - /tmp
      - /var/run
      - /var/log
```

**Step 3: Mount volumes for persistent writes**

```yaml
services:
  app:
    image: my-app
    read_only: true
    volumes:
      - app-data:/var/lib/app
      - ./logs:/var/log/app

volumes:
  app-data:
```

**Step 4: Set environment-specific writable paths**

```yaml
services:
  app:
    image: my-app
    read_only: true
    tmpfs:
      - /tmp:rw,noexec,nosuid,size=100m
```

**Step 5: Check for common writable path requirements**

```yaml
services:
  app:
    image: my-app
    read_only: true
    tmpfs:
      - /tmp
      - /var/run
      - /var/lib/nginx/tmp  # nginx needs writable tmp
```

## Common Mistakes

- **Setting read_only: true without any tmpfs mounts**: Most applications need to write to /tmp or /var/run.
- **Not checking which paths the application writes to**: Read the application logs to find the exact paths.
- **Mounting volumes at the wrong paths**: Ensure the writable mount paths match the application expectations.
- **Setting read_only on databases**: Do not set read_only on databases; they need to write to /var/lib.

## Related Pages

- [Docker Compose Volume Error](/tools/docker-compose/docker-compose-volume-error/) -- Volume mount issues
- [Docker Compose tmpfs Error](/tools/docker-compose/docker-compose-tmpfs-error/) -- tmpfs mount errors
- [Docker Compose Secrets Error](/tools/docker-compose/docker-compose-secrets-error/) -- Secrets issues
