---
title: "[Solution] Docker Compose Secrets Error — Fix Secrets Not Available / Mount Failed"
description: "Fix Docker Compose secrets errors when secret files or environment variables fail to mount. Resolve file permissions, path issues, and secret definition problems."
---

## What This Error Means

Docker Compose secrets errors occur when a container cannot access secrets defined in the compose file. Secrets may fail to mount as files or environment variables due to configuration issues.

A typical error:

```
ERROR: Secret "db_password" not found
```

Or:

```
ERROR: secrets must be pre-existing in a Docker Swarm when not using "external: true" with "file:" key
```

## What This Error Means (continued)

Non-Swarm compose files use `file:` key secrets that map directly. Swarm-mode secrets require different syntax.

## Why It Happens

Secrets errors happen when:

- **Secret file does not exist**: The file path specified in the secret definition is missing.
- **Wrong secret syntax**: Using Swarm-style secrets without Swarm mode.
- **Permission denied**: The secret file has restrictive permissions preventing Docker from reading it.
- **Secret name mismatch**: The service references a secret name that does not match the secrets definition.
- **External secret not created**: The external secret was not created in the Swarm.
- **Path collision**: The secret targets a path already occupied by a volume or another file.

## How to Fix It

**Step 1: Use file-based secrets (non-Swarm)**

```yaml
services:
  app:
    image: my-app
    secrets:
      - db_password

secrets:
  db_password:
    file: ./secrets/db_password.txt
```

**Step 2: Create the secret file**

```bash
mkdir -p secrets
echo "mysecretpassword" > secrets/db_password.txt
```

**Step 3: Set correct permissions**

```bash
chmod 600 secrets/db_password.txt
```

**Step 4: Use environment variable secrets**

```yaml
services:
  app:
    image: my-app
    secrets:
      - db_password
    environment:
      - DB_PASSWORD_FILE=/run/secrets/db_password
```

**Step 5: For Swarm mode, create the secret first**

```bash
echo "mysecret" | docker secret create db_password -
```

```yaml
services:
  app:
    image: my-app
    secrets:
      - db_password

secrets:
  db_password:
    external: true
```

**Step 6: Customize secret mount path**

```yaml
services:
  app:
    image: my-app
    secrets:
      - source: db_password
        target: /etc/app/db_password
        mode: 0400
```

## Common Mistakes

- **Using Swarm secret syntax without Swarm mode**: Use `file:` key for non-Swarm docker-compose.
- **Not creating secret files before deploying**: The file must exist before `docker compose up`.
- **Setting world-readable permissions on secret files**: Use chmod 600 for sensitive files.
- **Not checking if the secret file path is correct**: Use absolute or compose-relative paths.

## Related Pages

- [Docker Compose Volume Error](/tools/docker-compose/docker-compose-volume-error/) -- Volume mount issues
- [Docker Compose Readonly FS](/tools/docker-compose/docker-compose-readonly-fs/) -- Read-only filesystem
- [Docker Compose Build Error](/tools/docker-compose/docker-compose-build-error/) -- Build failures
