---
title: "[Solution] Poetry Keyring Backend Not Found Error — How to Fix"
description: "Fix Poetry keyring backend not found errors. Configure keyring backends, disable keyring for CI, and resolve credential storage issues in Poetry."
tools: ["poetry"]
error-types: ["keyring-error"]
severities: ["error"]
weight: 5
comments: true
---

This error means Poetry cannot access the system keyring to store or retrieve credentials. The keyring backend is not installed, not configured, or unavailable in the current environment.

## Why It Happens

- No keyring backend is installed in the Python environment
- The system keyring service (like GNOME Keyring or KDE Wallet) is not running
- Poetry is running in a headless environment (Docker, CI/CD) without a keyring service
- The `keyring` Python package is installed but not configured with a valid backend
- The DISPLAY environment variable is not set, preventing GUI keyring prompts
- A virtual environment does not inherit the system keyring configuration

## Common Error Messages

```
RuntimeError

No keyring backend found. Please install a keyring backend:
  pip install keyring
```

```
KeyringError

Failed to open keyring: No recommended backends were found.
```

```
RuntimeError

Unable to find a keyring backend. You can configure Poetry to not
use the keyring by setting the environment variable:
  POETRY_KEYRING_BACKEND=keyring.backends.null.Keyring
```

```
BackendError

Keyring backend 'keyring.backends.SecretService' failed to
initialize: D-Bus not available.
```

## How to Fix It

### 1. Install a Keyring Backend

```bash
pip install keyring
```

For specific backends:

```bash
# For Linux with SecretService (GNOME/KDE)
pip install keyring[keyring]

# For macOS Keychain
pip install keyring[mac]

# For Windows Credential Locker
pip install keyring[win]
```

### 2. Configure the Null Keyring (CI/CD)

In CI environments where keyring is not needed:

```bash
export POETRY_KEYRING_BACKEND=keyring.backends.null.Keyring
```

Or in `pyproject.toml`:

```toml
[tool.poetry]
keyring-backend = "keyring.backends.null.Keyring"
```

### 3. Set a Specific Keyring Backend

```bash
# List available backends
python -c "import keyring; print(keyring.backends.get_all_backends())"

# Set a specific backend
export POETRY_KEYRING_BACKEND=keyring.backends.SecretService.Keyring
```

### 4. Fix D-Bus Issues on Linux

```bash
# Start the D-Bus session
eval "$(dbus-launch)"

# Or run Poetry in an environment where D-Bus is available
```

For Docker containers:

```dockerfile
RUN apt-get update && apt-get install -y dbus libsecret-1-0
```

### 5. Use Environment Variables for Credentials

Instead of keyring, pass credentials via environment variables:

```bash
export POETRY_PYPI_TOKEN_PYPI=pypi-AgEI...your-token...
poetry publish
```

### 6. Disable Keyring in Poetry Config

```bash
poetry config keyring-backend keyring.backends.null.Keyring
```

### 7. Fix Virtual Environment Keyring Access

```bash
# Ensure keyring is installed in the venv
poetry run pip install keyring

# Or use the system keyring
poetry config --local virtualenvs.create false
```

## Common Scenarios

**Docker builds fail with keyring errors.** CI/CD and Docker containers lack keyring services. Disable keyring:

```bash
export POETRY_KEYRING_BACKEND=keyring.backends.null.Keyring
```

**Linux server without a display manager.** Install a non-GUI keyring backend:

```bash
pip install keyring[secretstorage]
```

**macOS Keychain prompts block automation.** Use environment variables for tokens:

```bash
export POETRY_PYPI_TOKEN_PYPI=pypi-AgEI...your-token...
poetry publish
```

## Prevent It

1. Always set `POETRY_KEYRING_BACKEND=keyring.backends.null.Keyring` in CI/CD pipelines and Docker containers
2. Use API tokens via environment variables for publishing in automated environments instead of relying on keyring
3. Install the appropriate keyring backend for your platform: `pip install keyring[<platform>]`
