---
title: "[Solution] Docker Compose Env Error — Fix Variable Not Set"
description: "Fix Docker Compose environment variable not set errors. Resolve missing variables, substitution issues, and .env file configuration."
---

## What This Error Means

The `environment variable not set` error means Docker Compose encountered an undefined variable during configuration parsing. Variable substitution failed because the variable is not defined in the environment, `.env` file, or compose file.

A typical error:

```
ERROR: The COMPOSE_PROJECT_NAME variable is not set
```

Or:

```
ERROR: Invalid interpolation format for "environment" option in service "web":
"${DB_PASSWORD}". You may need to escape any ":" with a backslash (\:).
```

## Why It Happens

Environment variable errors occur when:

- **Variable not defined anywhere**: The variable is referenced but not set in any source.
- **Missing .env file**: The compose file expects variables from a `.env` file that does not exist.
- **Wrong .env file location**: The `.env` file is not in the same directory as the compose file.
- **Shell environment not exported**: Variables are set in the shell but not exported.
- **Syntax errors in substitution**: Wrong `${VAR}` syntax or missing default values.

## How to Fix It

**Step 1: Create or check the .env file**

```bash
# Create .env file
cat > .env <<EOF
COMPOSE_PROJECT_NAME=myproject
DB_PASSWORD=secret
DB_NAME=mydb
APP_PORT=3000
EOF
```

**Step 2: Use default values in compose file**

```yaml
services:
  web:
    image: nginx
    ports:
      - "${APP_PORT:-8080}:80"
    environment:
      - DB_HOST=${DB_HOST:-localhost}
      - DB_PASSWORD=${DB_PASSWORD:?Set DB_PASSWORD in .env}
```

**Step 3: Pass environment variables explicitly**

```bash
# Set variables before running
export DB_PASSWORD=secret
docker compose up

# Or inline
DB_PASSWORD=secret docker compose up
```

**Step 4: Verify .env file is loaded**

```bash
# Check what variables Docker Compose sees
docker compose config

# List environment variables in container
docker compose exec web env
```

**Step 5: Use the correct env_file directive**

```yaml
services:
  web:
    image: nginx
    env_file:
      - ./config/web.env
      - .env
```

**Step 6: Fix variable substitution syntax**

```yaml
# WRONG - missing closing brace
environment:
  - DB_PORT=${DB_PORT

# CORRECT
environment:
  - DB_PORT=${DB_PORT}
  - DB_PORT=${DB_PORT:-5432}
```

## Common Mistakes

- **Putting .env in the wrong directory**: The `.env` file must be in the same directory as the compose file.
- **Not exporting shell variables**: Use `export VAR=value` not just `VAR=value`.
- **Using empty default values**: Use `${VAR:?Error message}` to require the variable.
- **Committing .env files with secrets**: Add `.env` to `.gitignore` and provide `.env.example` for documentation.

## Related Pages

- [Docker Compose Build Error](/tools/docker-compose/docker-compose-build-error/) — Image build failures
- [Docker Compose Version Error](/tools/docker-compose/docker-compose-version-error/) — Version compatibility issues
- [Ansible Undefined Variable](/tools/ansible/ansible-undefined-variable/) — Variable undefined errors
