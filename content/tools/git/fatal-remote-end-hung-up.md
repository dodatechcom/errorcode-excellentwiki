---
title: "[Solution] Git fatal: The remote end hung up unexpectedly"
description: "Fix 'The remote end hung up unexpectedly' error. Resolve Git connection drops during push, pull, or clone operations."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: The remote end hung up unexpectedly

fatal: The remote end hung up unexpectedly

This error occurs when the remote server closes the connection before the Git operation completes. The server terminated the connection prematurely.

## Common Causes

- Repository size is too large for the server
- Push exceeds server-side limits
- Network timeout or proxy disconnection
- Server-side git hooks rejecting the push
- Insufficient disk space on the server

## How to Fix

### Increase Git Buffer Size

```bash
git config --global http.postBuffer 524288000
```

### Use Shallow Clone

```bash
git clone --depth 1 <repo-url>
```

### Enable Compression

```bash
git config --global core.compression 9
```

### Push in Chunks

```bash
git push origin <branch> --no-progress
```

## Examples

```bash
# Example 1: Large repository push fails
git push origin main
# fatal: The remote end hung up unexpectedly
# Fix: git config --global http.postBuffer 524288000 && git push

# Example 2: Clone large repo
git clone https://github.com/user/large-repo.git
# fatal: The remote end hung up unexpectedly
# Fix: git clone --depth 1 https://github.com/user/large-repo.git

# Example 3: Check server hooks
git ls-remote origin
# If hooks reject push, contact repository admin
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
