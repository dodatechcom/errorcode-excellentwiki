---
title: "[Solution] Git fatal: early EOF"
description: "Fix 'early EOF' error. Resolve Git clone, fetch, or push failures when the connection is terminated before transfer completes."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: early EOF

fatal: early EOF

This error occurs when Git detects end-of-file before the expected data transfer completes. The network connection was terminated prematurely.

## Common Causes

- Unstable network connection
- Repository is too large for available bandwidth
- Server-side timeout
- Proxy or firewall interrupting long transfers
- Insufficient memory on client or server

## How to Fix

### Use Shallow Clone

```bash
git clone --depth 1 <url>
```

### Increase Buffer Size

```bash
git config --global http.postBuffer 524288000
git config --global http.lowSpeedLimit 0
git config --global http.lowSpeedTime 999999
```

### Enable Keep-Alive

```bash
git config --global http.keepAlive 120
```

### Use SSH Instead of HTTPS

```bash
git remote set-url origin git@github.com:user/repo.git
```

## Examples

```bash
# Example 1: Large repository clone
git clone https://github.com/user/large-repo.git
# fatal: early EOF
# Fix: git clone --depth 1 https://github.com/user/large-repo.git

# Example 2: Unstable connection
git config --global http.postBuffer 524288000
git config --global http.lowSpeedTime 300
git fetch origin

# Example 3: Use SSH for large transfers
git remote set-url origin git@github.com:user/repo.git
git fetch origin
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
