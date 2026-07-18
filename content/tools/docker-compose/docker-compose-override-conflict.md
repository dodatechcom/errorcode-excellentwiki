---
title: "[Solution] Docker Compose Override File Conflict Error — How to Fix"
description: "Fix Docker Compose override file merge conflicts. Resolve conflicting service definitions, duplicate keys, and override resolution issues fast."
comments: true
---

## What This Error Means

The override file conflict error occurs when Docker Compose cannot merge multiple compose files or when override files contain conflicting definitions that cannot be automatically resolved. Compose merges files in order, and later files override earlier ones.

A typical error:

```
ERROR: The Compose file './docker-compose.yml' is invalid:
services.web: duplicate key: "ports"
```

Or:

```
non-mapping "8080:80" at line 42 of docker-compose.override.yml
```

Or:

```
services.api.environment must be a mapping, not a list
```

Or:

```
yaml: unmarshal errors:
  line 15: key "image" already set in map
```

## Why It Happens

Override conflicts occur when:

- **Duplicate keys in same file**: The same YAML key appears twice in a mapping, which is invalid YAML.
- **Type mismatch in merge**: One file defines a key as a list and another defines it as a mapping.
- **Override adds incompatible keys**: An override file tries to add keys that conflict with the base file's structure.
- **Syntax errors in override file**: YAML syntax errors prevent Compose from parsing the override.
- **Multiple override files with conflicts**: Two different override files set the same service property to different values.
- **Incorrect override file naming**: The auto-loaded override file name does not follow the `docker-compose.override.yml` convention.

## Common Error Messages

### Duplicate key in YAML

```
yaml: unmarshal errors:
  line 20: key "environment" already set in map
```

The same key appears twice within a single service definition.

### Type conflict during merge

```
ERROR: The Compose file './docker-compose.override.yml' is invalid:
services.web.ports must be a list
```

One file defines `ports` as a string and another as a list, or vice versa.

### Invalid YAML syntax

```
ERROR: YAML parse error on docker-compose.override.yml:
mapping values are not allowed here
```

Indentation or syntax errors in the override file prevent parsing.

### Service not in base file

```
ERROR: The Compose file './docker-compose.override.yml' is invalid:
services.nonexistent: additional properties not allowed
```

The override file references a service that does not exist in the base compose file (in Compose V1 strict mode).

## How to Fix It

### Solution 1: Validate the compose files individually

Check each file for syntax errors before merging.

```bash
# Validate the base file
docker compose -f docker-compose.yml config

# Validate the override file
docker compose -f docker-compose.yml -f docker-compose.override.yml config

# Check YAML syntax with a linter
yamllint docker-compose.yml
yamllint docker-compose.override.yml
```

### Solution 2: Remove duplicate keys in YAML

Ensure each key appears only once per mapping in every compose file.

```yaml
# WRONG - duplicate "environment" key
services:
  web:
    image: nginx
    environment:
      - DEBUG=true
    environment:
      - PORT=80

# CORRECT - single "environment" key with all values
services:
  web:
    image: nginx
    environment:
      - DEBUG=true
      - PORT=80
```

### Solution 3: Match data types between base and override

Both files must use the same data type for the same key.

```yaml
# docker-compose.yml
services:
  web:
    image: nginx
    ports:
      - "80:80"        # List type

# docker-compose.override.yml - CORRECT (also a list)
services:
  web:
    ports:
      - "443:443"

# docker-compose.override.yml - WRONG (string type)
services:
  web:
    ports: "8080:80"   # This is a string, not a list
```

### Solution 4: Use environment-specific override files correctly

Name override files properly and control which ones are loaded.

```bash
# Auto-loaded (in order):
docker-compose.yml
docker-compose.override.yml

# Manual override files (explicitly specified):
docker-compose.prod.yml
docker-compose.dev.yml
docker-compose.test.yml
```

```bash
# Load base + specific override
docker compose -f docker-compose.yml -f docker-compose.prod.yml config

# Load base + multiple overrides (later files win)
docker compose \
  -f docker-compose.yml \
  -f docker-compose.override.yml \
  -f docker-compose.prod.yml \
  config
```

### Solution 5: Restructure to avoid merge conflicts

Reorganize compose files to minimize merge conflicts.

```yaml
# docker-compose.yml - minimal base configuration
services:
  web:
    image: nginx:latest
    networks:
      - frontend

  api:
    image: myapi:latest
    networks:
      - backend

networks:
  frontend:
  backend:

# docker-compose.override.yml - development additions only
services:
  web:
    ports:
      - "8080:80"
    volumes:
      - ./src:/app/src

  api:
    ports:
      - "8000:8000"
    volumes:
      - ./api:/app
```

### Solution 6: Resolve conflicting environment values

Use variable substitution to let one source of truth control values.

```yaml
# docker-compose.yml
services:
  api:
    environment:
      - LOG_LEVEL=${LOG_LEVEL:-info}
      - DB_HOST=${DB_HOST:-localhost}

# docker-compose.override.yml - do NOT override env vars here
# Let .env or shell environment control them
```

```bash
# Development .env
LOG_LEVEL=debug
DB_HOST=localhost

# Production environment
LOG_LEVEL=warn
DB_HOST=prod-db.internal
```

## Common Scenarios

### Git merge conflicts in compose files

Multiple developers modify the same compose file, creating merge conflicts.

```yaml
# After git merge - conflict markers
services:
  web:
<<<<<<< HEAD
    ports:
      - "8080:80"
=======
    ports:
      - "9090:80"
>>>>>>> feature-branch
```

Fix by using override files per environment instead of modifying the base file:

```yaml
# docker-compose.dev.yml (developer A)
services:
  web:
    ports:
      - "8080:80"

# docker-compose.dev.yml (developer B)
services:
  web:
    ports:
      - "9090:80"
```

Each developer uses their own override file that is gitignored.

### Override file accidentally committed

A `docker-compose.override.yml` with local configuration was committed to the repository, breaking builds on other machines.

```bash
# Add to .gitignore
echo "docker-compose.override.yml" >> .gitignore
```

Provide a template instead:

```bash
# docker-compose.override.example.yml (committed)
# Copy to docker-compose.override.yml for local customizations
services:
  web:
    ports:
      - "8080:80"
```

### Multiple overrides with conflicting network definitions

Two override files define the same network with different configurations.

```yaml
# docker-compose.dev.yml
networks:
  app-net:
    driver: bridge

# docker-compose.ci.yml
networks:
  app-net:
    driver: host    # CONFLICT
```

Resolve by using a single override that adapts to the environment:

```yaml
# docker-compose.override.yml
networks:
  app-net:
    driver: ${NETWORK_DRIVER:-bridge}
```

## Prevent It

- **Use `docker compose config` before committing**: Always validate the merged compose configuration after making changes. This catches duplicate keys, type mismatches, and invalid YAML before they reach the repository.
- **Keep the base compose file minimal and stable**: Put only essential, environment-agnostic configuration in `docker-compose.yml`. Move all environment-specific settings to override files that are either gitignored or clearly separated.
- **Standardize override file naming and documentation**: Document which override files exist, when each is used, and the correct load order. A `Makefile` with targets like `make dev`, `make test`, and `make prod` that invoke the correct compose file combinations eliminates confusion.
