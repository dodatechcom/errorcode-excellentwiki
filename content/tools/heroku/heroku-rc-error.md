---
title: "[Solution] Heroku CLI Configuration Error — How to Fix"
description: "Fix Heroku CLI configuration errors by resetting the .netrc file, updating authentication tokens, clearing the cache, and reinstalling the Heroku CLI."
tools: ["heroku"]
error-types: ["rc-error"]
severities: ["error"]
weight: 5
comments: true
---

A Heroku CLI configuration error occurs when the Heroku CLI cannot read or parse its configuration files, typically `.netrc` for authentication or `.heroku/config` for application settings. This prevents you from running any CLI commands.

## What This Error Means

The Heroku CLI relies on several configuration files stored in your home directory. The `.netrc` file stores your API token for authentication. The `.heroku` directory stores CLI preferences, plugin data, and cache. When these files are corrupted, have incorrect permissions, or are missing, the CLI throws configuration errors.

These errors are distinct from API errors like 401 Unauthorized (which means the token is wrong) — they occur before any API call is made, at the configuration parsing stage.

## Why It Happens

- `.netrc` file has incorrect permissions (must be 600)
- API token stored in `.netrc` is expired or invalid
- `.heroku` directory has corrupted JSON files
- CLI version mismatch after an update
- Multiple Heroku accounts with conflicting credentials
- Environment variables (`HEROKU_API_KEY`, `HEROKU_EMAIL`) conflict with local config
- The CLI cache is stale or corrupted

## Common Error Messages

```
 ▸    ENOENT: no such file or directory, open ~/.netrc
# or
 ▸    Error parsing heroku configuration: Unexpected token }
# or
 ▸    netrc file has incorrect permissions. Must be 600.
# or
 ▸    Heroku CLI internal error: Config file is not valid JSON
```

## How to Fix It

### 1. Check and Fix .netrc Permissions

```bash
# Check current permissions
ls -la ~/.netrc

# Fix permissions (must be readable only by owner)
chmod 600 ~/.netrc

# View contents (will show your API token)
cat ~/.netrc
```

The `.netrc` file must have permission `600` (`-rw-------`). Any other permissions cause the CLI to reject the file.

### 2. Re-authenticate with Heroku

```bash
# Login interactively
heroku login

# Or login with a browser token
heroku login -i

# Check current authentication status
heroku auth:whoami
heroku auth:token
```

Re-authentication regenerates the API token stored in `.netrc`. This fixes expired or invalid tokens.

### 3. Reset Configuration and Cache

```bash
# Backup and remove corrupted configuration
mv ~/.heroku ~/.heroku-backup

# Re-authenticate (this recreates the .heroku directory)
heroku login

# If that doesn't work, also clear any environment variables:
unset HEROKU_API_KEY
unset HEROKU_EMAIL
unset HEROKU_ORGANIZATION
```

### 4. Reinstall the Heroku CLI

```bash
# On macOS
brew uninstall heroku
brew install heroku

# On Ubuntu/Debian
sudo apt remove heroku
curl https://cli-assets.heroku.com/install-ubuntu.sh | sh

# Using npm
npm uninstall -g heroku
npm install -g heroku

# Verify installation
heroku --version
```

### 5. Use Environment Variables Instead of .netrc

```bash
# Set API key as environment variable (overrides .netrc)
export HEROKU_API_KEY="your-api-token-here"

# Get your API token from Heroku dashboard
heroku auth:token

# Run commands without .netrc
heroku apps
```

### 6. Check for Configuration File Conflicts

```bash
# Check if environment variables override local config
env | grep HEROKU

# Check for project-level .heroku/config.json
cat .heroku/config.json 2>/dev/null

# Check for multiple .netrc entries
grep -c "machine api.heroku.com" ~/.netrc

# If there are duplicate entries, remove the file and re-login
rm ~/.netrc
heroku login
```

### 7. Fix JSON Parse Errors in Config Files

```bash
# Validate JSON in config files
cat ~/.heroku/config.json | python -m json.tool

# If invalid, remove the corrupted files
rm ~/.heroku/config.json
rm ~/.heroku/plugin-cache.json

# Re-login to regenerate them
heroku login
```

## Common Scenarios

### CI/CD Pipeline Fails with .netrc Error

A GitHub Actions workflow installs the Heroku CLI and tries to run `heroku run migrate`. The `.netrc` file is not present in the CI environment. The fix is to use the `HEROKU_API_KEY` environment variable instead of relying on `.netrc`.

### After Upgrading Heroku CLI

After running `brew upgrade heroku`, CLI commands fail with configuration parsing errors. The new version expects a different config format. Back up and remove the `.heroku` directory, then run `heroku login` to regenerate the configuration.

### Multi-User Development Environment

Multiple developers share a Linux server, and each person's `.netrc` gets overwritten by another user's `heroku login` command. Each developer should use `HEROKU_API_KEY` environment variables or separate user accounts.

## Prevent It

- Use `HEROKU_API_KEY` environment variable in CI/CD environments instead of `.netrc`
- Set `.netrc` permissions correctly immediately after any Heroku login
- Keep the Heroku CLI updated to avoid config format incompatibilities
- Use separate user accounts or API keys for multi-developer environments
- Back up `.netrc` and `.heroku` directories before upgrading the CLI
- Validate configuration files with JSON parsers in automated scripts
- Use Heroku's `--remote` flag to manage multiple apps without config conflicts

## Related Pages

- [Heroku App Not Found](/tools/heroku/heroku-app-not-found)
- [Heroku Release Error](/tools/heroku/heroku-release-error)
- [Heroku Rate Limit Error](/tools/heroku/heroku-rate-limit-error)
