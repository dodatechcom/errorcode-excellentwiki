---
title: "[Solution] Git error: RPC failed; curl 56 OpenSSL SSL_read"
description: "Fix 'RPC failed; curl 56 OpenSSL SSL_read' error. Resolve Git push failures caused by SSL connection issues during large transfers."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git error: RPC failed; curl 56 OpenSSL SSL_read

error: RPC failed; curl 56 OpenSSL SSL_read: SSL_ERROR_SYSCALL, errno 0

This error occurs when Git fails to complete a large push or pull over HTTPS. The SSL/TLS connection drops unexpectedly during data transfer.

## Common Causes

- Large file sizes exceeding default buffer
- Slow or unstable network connection
- Server-side timeout during long transfers
- SSL/TLS negotiation failure
- Proxy or firewall interrupting long connections

## How to Fix

### Increase HTTP Post Buffer

```bash
git config --global http.postBuffer 524288000
```

### Use SSH Instead of HTTPS

```bash
git remote set-url origin git@github.com:user/repo.git
```

### Compress Data

```bash
git config --global core.compression 9
```

### Split Large Commits

```bash
git commit --amend -m "Split large files"
```

## Examples

```bash
# Example 1: Large push fails
git push origin main
# error: RPC failed; curl 56 OpenSSL SSL_read: SSL_ERROR_SYSCALL, errno 0
# Fix: git config --global http.postBuffer 524288000

# Example 2: Switch to SSH to avoid SSL issues
git remote set-url origin git@github.com:user/repo.git
git push origin main

# Example 3: Use Git LFS for large files
git lfs track "*.zip"
git add .gitattributes
git commit -m "Track large files with LFS"
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
