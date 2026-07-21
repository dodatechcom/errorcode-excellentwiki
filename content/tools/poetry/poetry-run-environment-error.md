---
title: "[Solution] Poetry Run Environment Error -- Fix Missing Environment Variables"
description: "Fix poetry run environment error when commands fail due to missing environment variables. Configure env vars for Poetry projects."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means a command run via `poetry run` failed because required environment variables are not set in the virtual environment.

## Common Causes

- `.env` file is not loaded automatically by Poetry
- Environment variables set in the shell are not passed to the venv
- The application expects specific env vars to be configured

## How to Fix

### 1. Use poetry run env to Check

```bash
poetry run env | grep -i myvar
```

### 2. Source .env Before Running

```bash
export $(cat .env | xargs) && poetry run python app.py
```

### 3. Use a Plugin to Load .env

```bash
poetry self add poetry-dotenv-plugin
```

### 4. Pass Variables Explicitly

```bash
MY_VAR=value poetry run python app.py
```

## Examples

```bash
$ poetry run python app.py
KeyError: 'DATABASE_URL'

$ export DATABASE_URL=postgresql://localhost/mydb
$ poetry run python app.py
Connected to database
```
