---
title: "[Solution] Docker Compose Version Error — Fix Incompatibility"
description: "Fix Docker Compose version incompatibility errors. Resolve compose file format issues, version conflicts, and feature compatibility."
---

## What This Error Means

Version errors occur when Docker Compose encounters syntax or features that are incompatible with the compose file version or the installed Docker Compose version.

A typical error:

```
ERROR: The Compose file './docker-compose.yml' is invalid because:
Unsupported config option for services.web: 'healthcheck'
```

Or:

```
ERROR: Version in docker-compose.yml is not supported.
Use docker compose (with a space) instead.
```

## Why It Happens

Version errors are caused by:

- **Using Docker Compose v1 syntax**: The `docker-compose` (v1) command is deprecated and does not support newer features.
- **Wrong version in compose file**: The version field specifies an unsupported format.
- **Feature requires newer version**: Features like `healthcheck`, `deploy`, or `depends_on.condition` need specific versions.
- **Docker Engine too old**: The Docker daemon does not support features required by the compose file.
- **Mixing v1 and v2 syntax**: Combining old and new syntax in the same file.

## How to Fix It

**Step 1: Upgrade Docker Compose to v2**

```bash
# Check version
docker compose version

# Install or upgrade
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker compose
sudo chmod +x /usr/local/bin/docker-compose
```

**Step 2: Remove the version field (recommended for v2)**

Docker Compose v2 infers the version automatically:

```yaml
# BEFORE (v1 style)
version: "3.8"
services:
  web:
    image: nginx

# AFTER (v2 style - no version field)
services:
  web:
    image: nginx
```

**Step 3: Update deprecated syntax**

```yaml
# v1 syntax (deprecated)
version: "2"
services:
  web:
    image: nginx
    depends_on:
      - api

# v2 syntax (current)
services:
  web:
    image: nginx
    depends_on:
      api:
        condition: service_healthy
```

**Step 4: Use the v2 command**

```bash
# OLD (v1)
docker-compose up

# NEW (v2)
docker compose up
```

**Step 5: Verify compose file compatibility**

```bash
docker compose config
```

## Common Mistakes

- **Still using `docker-compose` with a hyphen**: Migrate to `docker compose` (space-separated).
- **Specifying version in new compose files**: Omit the `version` field for Docker Compose v2.
- **Not upgrading Docker Desktop**: Docker Desktop includes Compose v2. Keep it updated.
- **Using features from newer versions with older compose files**: Remove the version field or upgrade to the latest format.

## Related Pages

- [Docker Compose Build Error](/tools/docker-compose/docker-compose-build-error/) — Image build failures
- [Docker Compose Env Error](/tools/docker-compose/docker-compose-env-error/) — Environment variable issues
- [Terraform Provider Error](/tools/terraform/terraform-provider-error/) — Version constraint issues
