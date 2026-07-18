---
title: "[Solution] Poetry Interactive Mode Error - Fix Non-Interactive Mode Error"
description: "Fix Poetry non-interactive mode errors when running in CI or automated scripts. Disable interactive prompts for headless environments."
tools: ["poetry"]
error-types: ["interactive-mode"]
severities: ["error"]
weight: 5
---

This error means Poetry is trying to show an interactive prompt but cannot because no TTY is attached. This is common in CI/CD pipelines, Docker builds, and automated scripts.

## What This Error Means

When Poetry needs user input but runs in a non-interactive context, you see:

```
PoetryException: Unable to create a virtual environment in non-interactive mode
# or
InputMissingError: No terminal, input disabled.
# or
error: this command requires an interactive terminal
```

This blocks operations that normally ask for confirmation, such as accepting new dependencies or creating virtual environments.

## Why It Happens

- You are running Poetry in a CI pipeline without a TTY
- The command is executed inside a Docker build without `--no-interaction`
- A script pipes input to Poetry which closes stdin
- Poetry prompts for confirmation on version conflicts but has no terminal
- The `VIRTUAL_ENV` is not set and Poetry tries to create one interactively
- An environment variable like `POETRY_VIRTUALENVS_CREATE` is not configured

## How to Fix It

### Use the --no-interaction flag

```bash
poetry install --no-interaction
```

This disables all interactive prompts and uses defaults.

### Set the environment variable

```bash
export POETRY_NO_INTERACTION=1
poetry install
```

This globally disables prompts for all Poetry commands.

### Pre-configure virtual environment settings

```bash
poetry config virtualenvs.create true
poetry config virtualenvs.in-project true
poetry install --no-interaction
```

If Poetry knows how to create venvs without asking, it works in non-interactive mode.

### Use poetry run with explicit venv activation

```bash
python -m venv .venv
source .venv/bin/activate
poetry install --no-interaction
```

Pre-creating the venv removes the need for Poetry to prompt about it.

### Handle version conflict confirmations

```bash
poetry add package@latest --no-interaction
```

Without `--no-interaction`, Poetry may ask "Would you like to proceed?" and hang.

### Use CI-specific Poetry configuration

```yaml
# In GitHub Actions
- run: |
    poetry config virtualenvs.create false
    poetry install
```

Disabling venv creation in CI avoids interactive prompts entirely.

## Common Mistakes

- Not passing `--no-interaction` in CI scripts and causing builds to hang
- Forgetting that Poetry prompts for confirmation on certain operations
- Running Poetry inside Docker without setting `POETRY_NO_INTERACTION`
- Not pre-installing dependencies needed for venv creation in CI images
- Assuming Poetry auto-detects non-interactive mode from stdin

## Related Pages

- [Poetry Install Error]({{< relref "/tools/poetry/poetry-install-error" >}}) -- installation failures
- [Poetry Venv Error]({{< relref "/tools/poetry/poetry-venv-error" >}}) -- virtual environment issues
- [Poetry Lock Error]({{< relref "/tools/poetry/poetry-lock-error" >}}) -- lock file problems
