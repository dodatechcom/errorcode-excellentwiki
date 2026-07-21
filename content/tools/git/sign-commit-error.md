---
title: "[Solution] Git Sign Commit Error"
description: "Fix Git GPG commit signing errors when signed commits fail verification."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
---

# Git Sign Commit Error

Git commit signing with GPG fails or commits show as unsigned.

```
error: gpg failed to sign the data
fatal: failed to write commit object
```

## Common Causes

- GPG key not configured in Git
- GPG agent not running
- Wrong key ID specified
- GPG passphrase not cached
- Key expired or revoked

## How to Fix

### Configure GPG Signing

```bash
# List available GPG keys
gpg --list-secret-keys --keyid-format=long

# Set signing key
git config --global user.signingkey ABCDEF1234567890

# Enable signing by default
git config --global commit.gpgsign true
```

### Start GPG Agent

```bash
# Start gpg-agent
gpg-agent --daemon

# Set GPG program path
git config --global gpg.program /usr/bin/gpg2
```

### Sign Commits

```bash
# Sign specific commit
git commit -S -m "Signed commit"

# Sign all commits by default
git config --global commit.gpgsign true

# Sign push
git push --signed
```

### Fix Passphrase Issues

```bash
# Cache passphrase for 1 hour
echo "expire-ttl 3600" | gpgconf --change-agent gpg-agent

# Check agent config
gpgconf --list-components
```

### Export and Import Key

```bash
# Export public key
gpg --armor --export ABCDEF1234567890

# Import key on another machine
gpg --import public-key.asc
```

## Examples

```bash
# Full GPG setup
gpg --full-generate-key
gpg --list-secret-keys
git config --global user.signingkey $(gpg --list-secret-keys --keyid-format=long | grep sec | awk '{print $2}' | cut -d'/' -f2)
git config --global commit.gpgsign true
```
