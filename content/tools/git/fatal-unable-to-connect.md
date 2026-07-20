---
title: "[Solution] Git fatal: unable to connect"
description: "Fix 'unable to connect' error. Resolve Git network connection failures to remote repository servers."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: unable to connect

fatal: unable to connect to <hostname>

This error occurs when Git cannot establish a TCP connection to the remote server. The server may be down, blocked by a firewall, or unreachable from your network.

## Common Causes

- Remote server is down or unreachable
- Firewall blocking outbound connections
- VPN not connected (for private repositories)
- SSH port (22) or HTTPS port (443) blocked
- Corporate proxy configuration missing

## How to Fix

### Check Connectivity with curl

```bash
curl -I https://github.com
```

### Test SSH Connection

```bash
ssh -T git@github.com
```

### Configure Proxy

```bash
git config --global http.proxy http://proxy:8080
git config --global https.proxy https://proxy:8080
```

### Check Firewall Rules

```bash
sudo iptables -L -n
```

### Use Different Protocol

```bash
# Switch from SSH to HTTPS
git remote set-url origin https://github.com/user/repo.git
```

## Examples

```bash
# Example 1: Server unreachable
git fetch origin
# fatal: unable to connect to github.com
# Fix: check internet connection or try later

# Example 2: SSH port blocked
git clone git@github.com:user/repo.git
# fatal: unable to connect to github.com:22
# Fix: git clone https://github.com/user/repo.git (use HTTPS)

# Example 3: Proxy configuration
git config --global http.proxy http://proxy.company.com:8080
git config --global https.proxy http://proxy.company.com:8080
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
