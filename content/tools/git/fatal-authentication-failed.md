---
title: "[Solution] Git fatal: Authentication failed"
description: "Fix 'Authentication failed' error. Resolve Git credential issues when pushing, pulling, or cloning from remote repositories."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: Authentication failed

fatal: Authentication failed for 'https://github.com/user/repo.git'

This error occurs when Git cannot authenticate your identity with the remote server. This typically happens with incorrect credentials, expired tokens, or SSH key issues.

## Common Causes

- Incorrect username or password
- Expired or revoked personal access token
- Two-factor authentication enabled without a token
- SSH key not added to your GitHub/GitLab account
- Credential helper has stale or wrong credentials

## How to Fix

### Use a Personal Access Token

```bash
git remote set-url origin https://<token>@github.com/user/repo.git
```

### Update Credential Helper

```bash
git credential reject
git credential approve
```

### Switch to SSH Authentication

```bash
git remote set-url origin git@github.com:user/repo.git
```

### Clear Cached Credentials

```bash
git config --global --unset credential.helper
git config --global credential.helper cache
```

## Examples

```bash
# Example 1: Token expired
git push origin main
# fatal: Authentication failed for 'https://github.com/user/repo.git'
# Fix: generate new token at GitHub Settings > Developer settings > Personal access tokens

# Example 2: Switch to SSH
git remote set-url origin git@github.com:user/repo.git
git push origin main

# Example 3: macOS Keychain reset
git credential-osxkeychain erase
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
