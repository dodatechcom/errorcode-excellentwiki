---
title: "[Solution] Git fatal: Unable to access URL"
description: "Fix 'unable to access' error. Resolve Git HTTP/HTTPS connection failures when accessing remote repositories."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: Unable to access URL

fatal: unable to access 'https://github.com/user/repo.git/'

This error occurs when Git cannot establish an HTTP or HTTPS connection to the remote repository URL. This is a network-level connectivity issue.

## Common Causes

- No internet connection or DNS resolution failure
- Proxy server blocking or requiring configuration
- Firewall blocking outbound connections
- SSL/TLS certificate verification failure
- Repository URL is malformed

## How to Fix

### Check Internet Connectivity

```bash
ping github.com
```

### Configure Git Proxy

```bash
git config --global http.proxy http://proxy:8080
git config --global https.proxy http://proxy:8080
```

### Disable SSL Verification (temporary)

```bash
git config --global http.sslVerify false
```

### Check DNS Resolution

```bash
nslookup github.com
```

### Use Correct URL Format

```bash
git remote set-url origin https://github.com/user/repo.git
```

## Examples

```bash
# Example 1: Proxy required at work
git clone https://github.com/user/repo.git
# fatal: unable to access 'https://github.com/user/repo.git/'
# Fix: git config --global http.proxy http://proxy.company.com:8080

# Example 2: SSL certificate issue
git config --global http.sslVerify false
# Or set correct CA bundle:
git config --global http.sslCAInfo /path/to/cert.pem

# Example 3: DNS resolution issue
echo "140.82.112.4 github.com" >> /etc/hosts
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
