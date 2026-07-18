---
title: "[Solution] Docker Compose V2 Migration Error — How to Fix"
description: "Fix Docker Compose V2 compatibility issues. Resolve migration errors from V1 to V2, command differences, and compose file format problems."
comments: true
---

## What This Error Means

The Compose V2 migration error occurs when transitioning from Docker Compose V1 (`docker-compose` with a hyphen) to V2 (`docker compose` as a Docker CLI subcommand). The two versions have different syntax, features, and compose file format support.

A typical error:

```
docker-compose: command not found
```

Or:

```
ERROR: Version in "./docker-compose.yml" is unsupported.
```

Or:

```
ERROR: The Compose file './docker-compose.yml' is invalid because:
Unsupported config option for services.web: 'networks'
```

Or:

```
unknown flag: --compatibility
```

## Why It Happens

Migration errors occur when:

- **Command syntax changed**: V1 uses `docker-compose` (hyphenated standalone binary), V2 uses `docker compose` (Docker CLI plugin).
- **Compose file version mismatch**: V1 supported `version: "2"` and `version: "3"`, V2 defaults to the latest spec and handles version fields differently.
- **Deprecated directives**: Some V1-era directives are no longer valid or have been renamed.
- **Feature parity gaps**: Certain V1 features were reimplemented differently in V2.
- **Python vs. Go implementation**: V1 was Python-based, V2 is Go-based, causing subtle behavioral differences in variable interpolation and path resolution.
- **Installed alongside each other**: Both V1 and V2 may be installed, causing command confusion.

## Common Error Messages

### Standalone binary not found

```
bash: docker-compose: command not found
```

V1 has been uninstalled or was never installed. Only the V2 plugin is available.

### Unsupported version field

```
ERROR: Version in "./docker-compose.yml" is unsupported.
```

The compose file specifies a version that the installed Compose binary does not support.

### Deprecated directive

```
ERROR: The Compose file './docker-compose.yml' is invalid because:
Unsupported config option for services.web: 'container_name'
```

This error appears when the compose file uses features from a version that conflicts with the declared version field.

### Subcommand not recognized

```
unknown command "docker-compose"
```

You are trying to use V1 syntax with the V2 binary. V2 does not support the standalone binary command format.

## How to Fix It

### Solution 1: Update commands from V1 to V2 syntax

Replace all `docker-compose` calls with `docker compose` (space instead of hyphen).

```bash
# V1 syntax (deprecated)
docker-compose up -d
docker-compose down
docker-compose logs -f

# V2 syntax (current)
docker compose up -d
docker compose down
docker compose logs -f
```

Update scripts and aliases:

```bash
# Remove old alias
unalias docker-compose 2>/dev/null

# Add V2 compatibility alias if needed
alias docker-compose='docker compose'
```

### Solution 2: Fix compose file version declarations

V2 handles the `version` field more flexibly. You can either remove it or update it.

```yaml
# BEFORE - explicit version may cause conflicts
version: "3.8"
services:
  web:
    image: nginx:latest

# AFTER - omit version for V2 best practice
services:
  web:
    image: nginx:latest
```

If you need to keep the version field, use a supported value:

```yaml
version: "3.9"
services:
  web:
    image: nginx:latest
```

### Solution 3: Install Docker Compose V2 plugin

If V2 is not installed, add the Docker CLI plugin.

```bash
# On Ubuntu/Debian
sudo apt-get update
sudo apt-get install docker-compose-plugin

# On CentOS/RHEL
sudo yum install docker-compose-plugin

# Verify installation
docker compose version

# If the plugin is not in PATH, download manually
mkdir -p ~/.docker/cli-plugins
curl -SL https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 \
  -o ~/.docker/cli-plugins/docker-compose
chmod +x ~/.docker/cli-plugins/docker-compose
```

### Solution 4: Fix V1-specific features not in V2

Some V1 features require adjustments for V2 compatibility.

```yaml
# V1 supported 'links' (deprecated in V2)
services:
  web:
    links:
      - db

# V2 - use networks instead
services:
  web:
    networks:
      - app-network
  db:
    networks:
      - app-network

networks:
  app-network:
```

Update the `build` section if using V1-style shorthand:

```yaml
# V1 shorthand
services:
  web:
    build: ./app

# V2 equivalent (both work, but explicit is better)
services:
  web:
    build:
      context: ./app
      dockerfile: Dockerfile
```

### Solution 5: Migrate environment variable syntax

V2 handles variable interpolation slightly differently.

```bash
# Check for V1-specific env var patterns
grep -n '\${' docker-compose.yml
```

```yaml
# V1 allowed some unset variable patterns
services:
  web:
    image: ${IMAGE_NAME}

# V2 - set defaults for missing variables
services:
  web:
    image: ${IMAGE_NAME:-nginx:latest}
```

### Solution 6: Validate the migrated compose file

```bash
# Check the config parses correctly
docker compose config

# Test with dry run
docker compose up --dry-run

# Compare V1 and V2 output
docker-compose config > v1-output.yml 2>/dev/null
docker compose config > v2-output.yml
diff v1-output.yml v2-output.yml
```

## Common Scenarios

### CI/CD pipeline still using V1

Build servers often have V1 installed from older base images. The pipeline fails with `command not found` after upgrading local Docker.

```yaml
# .github/workflows/deploy.yml
steps:
  - name: Install Compose V2
    run: |
      mkdir -p ~/.docker/cli-plugins
      curl -SL https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 \
        -o ~/.docker/cli-plugins/docker-compose
      chmod +x ~/.docker/cli-plugins/docker-compose

  - name: Start services
    run: docker compose up -d
```

### Team members on mixed versions

Some developers have V1, others have V2. The compose file must work with both during the transition.

```yaml
# Compatible format that works with both V1 and V2
version: "3.9"
services:
  web:
    image: nginx:latest
    ports:
      - "8080:80"
```

Standardize on V2 across the team:

```bash
# Add to Makefile or project scripts
.PHONY: up down logs

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f
```

### Python-dependent V1 scripts breaking

V1 required Python and pip. After removing Python or upgrading the system, V1 stops working entirely.

```bash
# Check if V1 is installed via pip
pip3 list | grep docker-compose

# Remove V1 completely
pip3 uninstall docker-compose

# Install V2 plugin instead
sudo apt-get install docker-compose-plugin
```

## Prevent It

- **Standardize on V2 across all environments**: Set a project policy that all developers, CI runners, and deployment servers use Docker Compose V2. Document this requirement in the project README and add a version check to your Makefile or entrypoint scripts.
- **Remove the `version` field from compose files**: The `version` key is now optional in V2 and can cause compatibility issues when it conflicts with the features used. Omitting it lets V2 use the latest spec automatically.
- **Automate compose version detection in scripts**: Add a preflight check to all deployment scripts that verifies the compose binary exists and reports its version. This catches migration gaps early and provides a clear error message instead of a cryptic failure deep in the deployment process.
