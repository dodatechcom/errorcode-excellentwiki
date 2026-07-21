---
title: "[Solution] Git Credential Manager Error"
description: "Fix Git credential manager errors when cached credentials fail or need to be reset."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
---

# Git Credential Manager Error

Git credential manager fails to retrieve or store credentials correctly.

```
fatal: Authentication failed for 'https://github.com/user/repo.git'
```

## Common Causes

- Cached credentials are expired or revoked
- Credential helper not configured
- Multiple credential helpers conflicting
- Token format incorrect
- Credential store file corrupted

## How to Fix

### Clear Cached Credentials

```bash
# Remove specific credential
git credential reject <<EOF
protocol=https
host=github.com
EOF

# Clear entire credential cache
git config --global --unset credential.helper
git credential-cache exit
```

### Configure Credential Helper

```bash
# Use cache (in-memory)
git config --global credential.helper cache

# Use store (file-based)
git config --global credential.helper store

# Use macOS Keychain
git config --global credential.helper osxkeychain

# Use Windows Credential Manager
git config --global credential.helper manager
```

### Reset Credentials for Specific Host

```bash
# Clear credentials for GitHub
git credential reject <<EOF
protocol=https
host=github.com
EOF
```

### Check Credential Helper

```bash
# See configured helper
git config --global --get credential.helper

# List all credential-related config
git config --global --list | grep credential
```

## Examples

```bash
# Full credential reset workflow
git config --global --unset credential.helper
git config --global credential.helper store

# Next push will prompt for credentials
git push

# Verify credentials are stored
cat ~/.git-credentials
```
