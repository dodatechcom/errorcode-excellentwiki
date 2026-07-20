---
title: "[Solution] Git credential cache error"
description: "Fix Git credential cache errors. Resolve issues when Git credential caching is not working or fails to save credentials."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git credential cache error

fatal: credential-cache unavailable; no unix socket support

This error occurs when the credential cache helper cannot be used because the system does not support Unix sockets (e.g., Windows, or certain container environments).

## Common Causes

- Windows or unsupported environment for credential cache
- Git installed without socket support
- Running in a minimal container
- Credential cache timeout expired
- Permission issues with socket directory

## How to Fix

### Use Store Helper (less secure)

```bash
git config --global credential.helper store
```

### Use Manager (Windows)

```bash
git config --global credential.helper manager
```

### Increase Cache Timeout

```bash
git config --global credential.helper "cache --timeout=86400"
```

### Clear Credential Cache

```bash
git credential-cache exit
```

## Examples

```bash
# Example 1: Windows credential manager
git config --global credential.helper manager-core

# Example 2: Store credentials with timeout
git config --global credential.helper "cache --timeout=3600"

# Example 3: Use plaintext store (Linux)
git config --global credential.helper store
# Credentials saved to ~/.git-credentials
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
